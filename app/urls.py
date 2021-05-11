from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls, name='urls-all'),
    path('<str:id>/', views.redirector, name='urls-redirect')
    ]