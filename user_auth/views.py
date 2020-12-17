from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from core.views import index
from user_auth.forms import AuthenticateForm
from user_auth.utils import create_user

User = get_user_model()


def register_view(request):
    form = AuthenticateForm
    template_name = 'register.html'
    context = {'form': form}

    if request.GET:
        return render(request, template_name=template_name, context={'form': form})

    if request.POST:
        form = form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = create_user(
                    username=username,
                    password=password
                )
                login(request, user)
            except IntegrityError:
                return redirect(login_view)
        return redirect(index)
    return render(request, template_name=template_name, context=context)


def login_view(request):
    form = AuthenticateForm
    template_name = 'login.html'
    context = {'form': form}

    if request.GET:
        return render(request, template_name=template_name, context={'form': form})

    if request.POST:
        form = form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                login(request, user)
            except AttributeError:
                return redirect(register_view)

        return redirect(index)
    return render(request, template_name=template_name, context=context)


def logout_view(request):
    username = request.user.username
    logout(request)
    if username == 'test':
        User.objects.filter(username=username).delete()
    return redirect(index)
