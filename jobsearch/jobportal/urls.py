from django.contrib import admin
from django.urls import include, path

from jobportal import views

urlpatterns = [
    path('home/', views.index, name='home'),
]
