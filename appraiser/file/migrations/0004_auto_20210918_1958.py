# Generated by Django 2.2.19 on 2021-09-18 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20210918_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filetoken',
            options={'ordering': ['-tf']},
        ),
    ]
