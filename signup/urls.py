from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.index, name='index'),
    path('final/', views.web_detail_create, name='web_detail_create')
]
