from django.urls import path
from .views import index

appname = 'signup'
urlpatterns = [
    path('', index, name='index'),
]
