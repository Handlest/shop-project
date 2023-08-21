from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


def register(request):
    error_text = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error_text = 'Пожалуйста, проверьте правильность введённых данных'
    form = RegisterForm()
    data = {
        'form': form,
        'error': error_text
    }
    return render(request, 'authentication/register.html', data)


def login_user(request):
    error_text = ''
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            error_text = 'Проверьте данные авторизации'
    form = LoginForm()
    data = {
        'form': form,
        'error': error_text
    }
    return render(request, 'authentication/login.html', data)