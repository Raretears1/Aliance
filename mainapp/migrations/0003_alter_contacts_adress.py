# Generated by Django 3.2.5 on 2021-07-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='adress',
            field=models.CharField(max_length=100, verbose_name='Адреса'),
        ),
    ]
