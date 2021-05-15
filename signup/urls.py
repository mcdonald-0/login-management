from django.urls import path
from .views import index, current_datetime

appname = 'signup'
urlpatterns = [
    path('', index, name='index'),
    path('time/', current_datetime)
]
