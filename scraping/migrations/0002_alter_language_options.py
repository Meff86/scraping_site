# Generated by Django 4.1 on 2022-09-05 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name': 'Язык программирования', 'verbose_name_plural': 'Языки программирования'},
        ),
    ]
