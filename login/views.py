from django.shortcuts import render, redirect
from .forms import LoginForm


def index(requests):
    return render(requests, 'login/index.html', {})


def dashboard(requests):
    return render(requests, "users/dashboard.html", {})

def login(requests):
    form = LoginForm()
    if requests.method == "POST":
        form = LoginForm(requests.POST)
        if form.is_valid():
            print('hello')
            # WebDetail.objects.get(**form.cleaned_data)

    context = {'form': form}
    return render(requests, 'registration/login.html', context)



# TODO: i need to create a login page so a guest can either login  or signup for now, its just the signup
#   that works so i need to create a login form inside the signup directory.


# TODO: i need to research on adding css, images, javascript and bootstrap to my project
