from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(requests):
    return HttpResponse('<h1>Congratulations</h1>')
