from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ContactForm
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def shop(request):
    Games = Game.objects.all()
    context = {'games': Games,
               }
    return render(request, 'shop.html', context)


def cart(request):
    return render(request, 'cart.html')


# Create your views here.
def sign_up(request):
    Buyers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            balance = form.cleaned_data['balance']
            age = form.cleaned_data['age']
            for buyer in Buyers:
                if buyer.name == name:
                    info["error"] = 'Пользователь уже существует'
            if not info:
                Buyer.objects.create(name=name, balance=float(balance), age=int(age))
                return HttpResponse(f'Приветствуем, {name}!')
    else:
        form = ContactForm()
    return render(request, 'registration_page.html', info)


def news(request):
    all_news = News.objects.all().order_by('-date')
    paginator = Paginator(all_news, 3)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': news})
