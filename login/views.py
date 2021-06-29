from django.shortcuts import render


def index(requests):
    return render(requests, 'login/index.html')

# TODO: i need to link the authentication url to the various templates because its just showing django
#   default templates
