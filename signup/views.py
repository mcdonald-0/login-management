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
            user = form.save()
            User.objects.create(**form.cleaned_data)
            requests.session['data'] = form.cleaned_data
            return redirect('signup:web_detail_create')
    context = {'form': form}
    return render(requests, 'signup/index.html', context)


def web_detail_create(requests):
    form = UserDetailForm()
    user_detail = requests.session.get('data')
    print(requests.user)
    if requests.method == "POST":
        form = UserDetailForm(requests.POST)
        if form.is_valid():
            print(user_detail['password'])
            User.objects.create_user(**form.cleaned_data)
            form.save()
            user = User.objects.get(username=user_detail['username'])
            UserDetail.objects.create(user=user)
            return HttpResponse('<h1>Congratulations</h1>')
    context = {'form': form}
    return render(requests, 'signup/final.html', context)

# TODO: i need to link all of this in one form that inherits from the django.auth.User

# TODO: i need to add bootstrap to my projects for stylish looks
