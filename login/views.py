from django.shortcuts import render, redirect


def index(requests):
    return render(requests, 'login/index.html', {})


def dashboard(requests):
    return render(requests, "users/dashboard.html", {})

# TODO: i need to create a login page so a guest can either login  or signup for now, its just the signup
#   that works so i need to create a login form inside the signup directory.
