# Generated by Django 4.2.8 on 2023-12-27 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='questions',
            new_name='question',
        ),
    ]