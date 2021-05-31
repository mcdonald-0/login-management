from django.urls import path, include
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sta/', views.static_view)
]
