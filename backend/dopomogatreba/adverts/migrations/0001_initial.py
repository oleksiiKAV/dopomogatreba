# Generated by Django 4.0.5 on 2022-06-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Логотип')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Название',
                'verbose_name_plural': 'Названия',
            },
        ),
    ]