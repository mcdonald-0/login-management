import random
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserDetailForm, UserCreateForm
from .models import UserDetail
from django.shortcuts import redirect, reverse, get_object_or_404


def index(requests):
    form = UserCreateForm()
    if requests.method == "POST":
        form = UserCreateForm(requests.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            requests.session['user_data'] = user
            return redirect('signup:web_detail_create')
    context = {'form': form}
    return render(requests, 'signup/index.html', context)


def web_detail_create(requests):
    form = UserDetailForm()
    print(requests.session.get('user_data'))
    if requests.method == "POST":
        form = UserDetailForm(requests.POST)
        if form.is_valid():
            user = UserDetail.objects.create(**form.cleaned_data)
            user.save()
            return HttpResponse('<h1>Congratulations</h1>')
    context = {'form': form}
    return render(requests, 'signup/final.html', context)




# TODO: i need to add bootstrap to my projects for stylish looks
