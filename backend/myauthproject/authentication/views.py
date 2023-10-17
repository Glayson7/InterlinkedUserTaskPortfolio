from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "authentication/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    # Aqui você adicionará a lógica de autenticação
    return render(request, "authentication/login.html", {"form": form})


def welcome(request):
    return HttpResponse("Bem-vindo ao meu projeto!")
