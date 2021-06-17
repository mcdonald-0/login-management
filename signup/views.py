from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import UserCreateForm, UserLoginForm
from .models import UserDetail


def index(requests):
    form = UserCreateForm()
    if requests.method == "POST":
        form = UserCreateForm(requests.POST)
        if form.is_valid():
            user = form.save()
            UserDetail.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender'],
                email=form.cleaned_data['email']
            )
            return redirect('/accounts/login')
    context = {'form': form}
    return render(requests, 'signup/index.html', context)


def user_login(requests):
    form = UserLoginForm()
    if requests.method == "POST":
        form = UserCreateForm(requests.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(requests, user)
                return redirect('blog:index')
            else:
                print('<h1>Sorry</h1>')
    context = {'form': form}
    return render(requests, 'signup/index.html', context)

