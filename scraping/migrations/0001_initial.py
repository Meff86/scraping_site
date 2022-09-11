# Generated by Django 4.1 on 2022-09-01 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название города')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Название города',
                'verbose_name_plural': 'Название городов',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Язык программирования',
                'verbose_name_plural': 'Язык программирования',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок вакансии')),
                ('company', models.CharField(max_length=250, verbose_name='Компания')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city',
                                           verbose_name='Город')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language',
                                               verbose_name='Язык программирования')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
