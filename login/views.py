from django.shortcuts import render


def index(requests):
    return render(requests, 'login/index.html', {})


def dashboard(requests):
    return render(requests, "users/dashboard.html", {})
