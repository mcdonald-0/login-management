from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils import timezone


def current_datetime(request):
    now = datetime.datetime.now()
    now2 = timezone.now()
    html = "<html><body>It is now %s.</body></html>" % now
    html2 = "<html><body>It is now %s.</body></html>" % now2
    return HttpResponse(html2)


def index(requests):
    return HttpResponse('<h1>You are welcomed</h1>')
