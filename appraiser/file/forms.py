from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from .models import File

def file_size(value):
    limit = 9 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 9 MiB.')

class FileModelForm(forms.ModelForm):
    file = forms.FileField(validators=[FileExtensionValidator( ['txt'] ) ])

    class Meta:
        model = File
        fields = ('name', 'file',)
