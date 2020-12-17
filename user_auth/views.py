from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout

from core.views import index
from user_auth.forms import AuthenticateForm
from user_auth.utils import create_user


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
    logout(request)
    return redirect(index)
