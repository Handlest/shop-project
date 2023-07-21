from django.shortcuts import render
from django.urls import reverse


def main_page(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def sales(request):
    return render(request, 'main/sales.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def faq(request):
    return render(request, 'main/faq.html')


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')