from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserDetailForm, WebDetailForm
from .models import UserDetail, WebDetail
from django.shortcuts import redirect, reverse


def index(requests):
    form = UserDetailForm()
    if requests.method == "POST":
        form = UserDetailForm(requests.POST)
        if form.is_valid():
            UserDetail.objects.create(**form.cleaned_data)
            item = UserDetail.objects.latest('id')
            return redirect('signup:web_detail_create', user=item)
    context = {'form': form}
    return render(requests, 'signup/index.html', context)


def web_detail_create(requests, user):
    form = WebDetailForm()
    if requests.method == "POST":
        form = UserDetailForm(requests.POST)
        if form.is_valid():
            # TODO: i need the function above to go with the users data and that would be refrenced as the user
            #   of the password and the username.
            WebDetail.objects.create(**form.cleaned_data)
            return redirect('signup:final')
    context = {'form': form}
    return render(requests, 'signup/final.html', context)
