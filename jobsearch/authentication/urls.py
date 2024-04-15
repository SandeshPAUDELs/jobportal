from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),  
    path('logout/', views.logoutUser, name='logout'),  
    path('', views.register, name='register'),
]