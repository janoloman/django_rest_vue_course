# Generated by Django 4.2.7 on 2023-12-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_author', models.CharField(max_length=40)),
                ('quote_body', models.CharField(max_length=60)),
                ('context', models.TextField()),
                ('created_at', models.DateField()),
            ],
        ),
    ]