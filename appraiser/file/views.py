import nltk
import math
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

import appraiser.settings as settings
from .models import Token, File, FileToken
from .forms import FileModelForm
from . import calculations


def index(request):
    files = File.objects.filter(owner=request.user)
    context = {'files': files}
    return render(request, 'index.html', context)


@login_required
def upload(request):
    form = FileModelForm(request.POST or None, files=request.FILES or None)
    context = {'form': form}

    def create_token(tokens, count_all, file):
        to_text = nltk.Text(tokens)
        fdist = nltk.FreqDist(to_text)
        files = File.objects.filter(owner=request.user).count()
        for token, count_t in fdist.items():
            current_token, status = Token.objects.get_or_create(
                word=token)
            FileToken.objects.get_or_create(
                token=current_token, file=file, tf=count_t/count_all
            )
            count_D_with_t = FileToken.objects.filter(
                file__owner=request.user, token=current_token).count()
            current_token.idf = math.log(files/count_D_with_t)
            current_token.save()

    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        obj.save()
        text = calculations.import_text(obj.file.path)
        tokens = calculations.word_tokenize(calculations.clean_text(text))

        obj.tokens_counter = len(tokens)
        create_token(tokens, obj.tokens_counter, obj)
        return redirect('file_tf_idf', obj.name)
    return render(request, 'new.html', context)


@login_required
def file_tf_idf(request, file):
    file = get_object_or_404(File, name=file, owner=request.user)
    tokens = FileToken.objects.filter(file=file)[:50]
    context = {'file': file, 'tokens': tokens}
    return render(request, 'file.html', context)


@login_required
def dictionary(request):
    owner = request.user
    tokens = FileToken.objects.filter(file__owner=owner)[:50]
    context = {'tokens': tokens}
    return render(request, 'dictionary.html', context)


@login_required
def delete_file(request, id):
    file = get_object_or_404(File, id=id, owner=request.user)
    file.delete()
    return redirect('index')
