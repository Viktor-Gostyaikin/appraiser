from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.owner.username, filename)


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=200)
    idf = models.FloatField(default=0)

    class Meta:
        ordering = ['-idf']

    def __str__(self):
        return self.word


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Название')
    created = models.DateTimeField(
        verbose_name='date uploaded', auto_now_add=True)
    token = models.ManyToManyField(Token, through='FileToken', default=None)
    tokens_counter = models.IntegerField(
        verbose_name='count of tokens in file', default=0)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='file'
    )
    file = models.FileField(upload_to=user_directory_path,
                            blank=False, null=False, verbose_name='Текстовый файл')

    def __str__(self):
        return self.name


class FileToken(models.Model):
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='file_token')
    token = models.ForeignKey(
        Token, on_delete=models.CASCADE, related_name='token')
    tf = models.FloatField(default=None)

    class Meta:
        ordering = ['-token__idf']

    def __str__(self):
        return self.tf
