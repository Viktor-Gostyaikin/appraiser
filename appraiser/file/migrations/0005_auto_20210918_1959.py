# Generated by Django 2.2.19 on 2021-09-18 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_auto_20210918_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filetoken',
            options={'ordering': ['tf']},
        ),
    ]
