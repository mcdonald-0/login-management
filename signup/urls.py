from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
]
