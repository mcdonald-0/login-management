import random
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserDetailForm, WebDetailForm
from .models import UserDetail, WebDetail
from django.shortcuts import redirect, reverse, get_object_or_404


def index(requests):
    form = UserDetailForm()
    if requests.method == "POST":
        form = UserDetailForm(requests.POST)
        if form.is_valid():
            UserDetail.objects.create(**form.cleaned_data)
            return redirect('signup:web_detail_create')
    context = {'form': form}
    return render(requests, 'signup/index.html', context)


def web_detail_create(requests):
    form = WebDetailForm()
    if requests.method == "POST":
        form = UserDetailForm(requests.POST)
        if form.is_valid():
            WebDetail.objects.create(**form.cleaned_data)
            return redirect('signup:final')
    context = {'form': form}
    return render(requests, 'signup/final.html', context)

# TODO: i need to add bootstrap to my projects for stylish looks
