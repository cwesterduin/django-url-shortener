from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls, name='urls-all')
]