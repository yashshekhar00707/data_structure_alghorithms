from django.contrib import admin
from django.urls import path, include
from .views import fun1

urlpatterns = [
    path('', fun1, name='fun1'),
]