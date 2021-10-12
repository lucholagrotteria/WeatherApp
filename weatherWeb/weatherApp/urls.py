from django.urls import path
from weatherApp import views

urlpatterns = [
    path('', views.index, name='index')
]