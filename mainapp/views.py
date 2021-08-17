from django.shortcuts import render


from .models import Navbar, Contacts, Bucha, Irpin, Gostomel, Vorzel, Stoyanka, Kiev


def test_view(request):
    navbar = Navbar.objects.all()
    return render(request, 'main.html', {"navbar": navbar})


def contacts(request):
    contact = Contacts.objects.all()
    navbar = Navbar.objects.all()
    return render(request, 'info.html', {"navbar": navbar, "contact": contact})


def bucha(request):
    buchaa = Bucha.objects.all()
    contact = Contacts.objects.all()
    navbar = Navbar.objects.all()
    return render(request, 'bucha.html', {"navbar": navbar, "contact": contact, "buchaa": buchaa})


def irpin(request):
    irpinn = Irpin.objects.all()
    navbar = Navbar.objects.all()
    return render(request, 'irpin.html', {"navbar": navbar, "irpinn":irpinn})


def stoyanka(request):
    stoyy = Stoyanka.objects.all()
    navbar = Navbar.objects.all()
    return render(request, 'stoyanka.html', {"navbar": navbar, "stoyy":stoyy})


def gost(request):
    navbar = Navbar.objects.all()
    gosttt = Gostomel.objects.all()
    return render(request, 'gost.html', {"navbar": navbar, "gosttt": gosttt})


def vorzel(request):
    navbar = Navbar.objects.all()
    vorzell = Vorzel.objects.all()
    return render(request, 'vorzel.html', {"navbar": navbar, "vorzell":vorzell})

def kyiv(request):
    navbar = Navbar.objects.all()
    kievv = Kiev.objects.all()
    return render(request, 'kyiv.html', {"navbar": navbar, "kievv":kievv})

