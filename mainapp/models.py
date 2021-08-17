from django.db import models
from django.urls import reverse


class Navbar(models.Model):
    inst = models.CharField(max_length=1000, verbose_name='Instagram', primary_key='inst')
    facebook = models.CharField(max_length=1000, verbose_name='Facebook')
    email = models.CharField(max_length=1000, verbose_name='Gmail')
    number1 = models.CharField(max_length=13, verbose_name='Номер телефона #1')
    number2 = models.CharField(max_length=13, verbose_name='Номер телефона #2')

    def get_absolute_url(self):
        return reverse('navbar', kwargs={'pk': self.pk})

    def __str__(self):
        return self.email


class Contacts(models.Model):
    adress = models.CharField(max_length=100, verbose_name='Адреса')

    def get_absolute_url(self):
        return reverse('contact', kwargs={'pk': self.pk})

    def __str__(self):
        return self.adress


class Bucha(models.Model):
    city =  models.CharField(max_length=100, verbose_name='БУЧА')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    land = models.CharField(max_length=1000, verbose_name='Земля')
    houses = models.CharField(max_length=1000, verbose_name='Дома')
    flat = models.CharField(max_length=1000, verbose_name='Квартири')
    comerc = models.CharField(max_length=1000, verbose_name='Комерція')

    def get_absolute_url(self):
        return reverse('bucha', kwargs={'pk': self.pk})

    def __str__(self):
        return self.city


class Irpin(models.Model):
    city = models.CharField(max_length=100, verbose_name='ІРПІНЬ')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    land = models.CharField(max_length=1000, verbose_name='Земля')
    houses = models.CharField(max_length=1000, verbose_name='Дома')
    flat = models.CharField(max_length=1000, verbose_name='Квартири')
    comerc = models.CharField(max_length=1000, verbose_name='Комерція')

    def get_absolute_url(self):
        return reverse('irpin', kwargs={'pk': self.pk})

    def __str__(self):
        return self.city


class Gostomel(models.Model):
    city =  models.CharField(max_length=100, verbose_name='ГОСТОМЕЛЬ')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    land = models.CharField(max_length=1000, verbose_name='Земля')
    houses = models.CharField(max_length=1000, verbose_name='Дома')
    flat = models.CharField(max_length=1000, verbose_name='Квартири')
    comerc = models.CharField(max_length=1000, verbose_name='Комерція')

    def get_absolute_url(self):
        return reverse('gostomel', kwargs={'pk': self.pk})

    def __str__(self):
        return self.city


class Stoyanka(models.Model):
    city =  models.CharField(max_length=100, verbose_name='СТОЯНКА')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    land = models.CharField(max_length=1000, verbose_name='Земля')
    houses = models.CharField(max_length=1000, verbose_name='Дома')
    flat = models.CharField(max_length=1000, verbose_name='Квартири')
    comerc = models.CharField(max_length=1000, verbose_name='Комерція')

    def get_absolute_url(self):
        return reverse('stoyanka', kwargs={'pk': self.pk})

    def __str__(self):
        return self.city


class Vorzel(models.Model):
    city =  models.CharField(max_length=100, verbose_name='ВОРЗЕЛЬ')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    land = models.CharField(max_length=1000, verbose_name='Земля')
    houses = models.CharField(max_length=1000, verbose_name='Дома')
    flat = models.CharField(max_length=1000, verbose_name='Квартири')
    comerc = models.CharField(max_length=1000, verbose_name='Комерція')

    def get_absolute_url(self):
        return reverse('vorzel', kwargs={'pk': self.pk})

    def __str__(self):
        return self.city


class Kiev(models.Model):
    city =  models.CharField(max_length=100, verbose_name='КИЇВ')
    text = models.CharField(max_length=1000, verbose_name='Текст')
    land = models.CharField(max_length=1000, verbose_name='Земля')
    houses = models.CharField(max_length=1000, verbose_name='Дома')
    flat = models.CharField(max_length=1000, verbose_name='Квартири')
    comerc = models.CharField(max_length=1000, verbose_name='Комерція')

    def get_absolute_url(self):
        return reverse('kiev', kwargs={'pk': self.pk})

    def __str__(self):
        return self.city
