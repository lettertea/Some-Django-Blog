# Generated by Django 2.0.1 on 2018-01-08 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
