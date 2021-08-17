# Generated by Django 3.2.5 on 2021-07-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_contacts_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='БУЧА')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('land', models.CharField(max_length=100, verbose_name='Земля')),
                ('houses', models.CharField(max_length=100, verbose_name='Дома')),
                ('flat', models.CharField(max_length=100, verbose_name='Квартири')),
                ('comerc', models.CharField(max_length=100, verbose_name='Комерція')),
            ],
        ),
        migrations.CreateModel(
            name='Gostomel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='ГОСТОМЕЛЬ')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('land', models.CharField(max_length=100, verbose_name='Земля')),
                ('houses', models.CharField(max_length=100, verbose_name='Дома')),
                ('flat', models.CharField(max_length=100, verbose_name='Квартири')),
                ('comerc', models.CharField(max_length=100, verbose_name='Комерція')),
            ],
        ),
        migrations.CreateModel(
            name='Irpin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='ІРПІНЬ')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('land', models.CharField(max_length=100, verbose_name='Земля')),
                ('houses', models.CharField(max_length=100, verbose_name='Дома')),
                ('flat', models.CharField(max_length=100, verbose_name='Квартири')),
                ('comerc', models.CharField(max_length=100, verbose_name='Комерція')),
            ],
        ),
        migrations.CreateModel(
            name='Kiev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='КИЇВ')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('land', models.CharField(max_length=100, verbose_name='Земля')),
                ('houses', models.CharField(max_length=100, verbose_name='Дома')),
                ('flat', models.CharField(max_length=100, verbose_name='Квартири')),
                ('comerc', models.CharField(max_length=100, verbose_name='Комерція')),
            ],
        ),
        migrations.CreateModel(
            name='Stoyanka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='СТОЯНКА')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('land', models.CharField(max_length=100, verbose_name='Земля')),
                ('houses', models.CharField(max_length=100, verbose_name='Дома')),
                ('flat', models.CharField(max_length=100, verbose_name='Квартири')),
                ('comerc', models.CharField(max_length=100, verbose_name='Комерція')),
            ],
        ),
        migrations.CreateModel(
            name='Vorzel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='ВОРЗЕЛЬ')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('land', models.CharField(max_length=1000, verbose_name='Земля')),
                ('houses', models.CharField(max_length=100, verbose_name='Дома')),
                ('flat', models.CharField(max_length=100, verbose_name='Квартири')),
                ('comerc', models.CharField(max_length=100, verbose_name='Комерція')),
            ],
        ),
    ]
