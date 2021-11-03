from django.urls import path
from . import views

urlpatterns = [
    path('url_shortener_app', views.shortener, name='shortener'),
    path('save/', views.save_url, name='save_url'),
    path('<str:code>/', views.redirect, name='redirect')
]