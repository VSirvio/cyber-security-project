from django.urls import path

from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('registerpage/', registerPageView, name='registerpage'),
    path('register/', registerView, name='register'),
    path('loginpage/', loginPageView, name='loginpage'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('listpage/', listPageView, name='listpage'),
    path('addingpage/', movieAddingPageView, name='addingpage'),
    path('add/', addView, name='add'),
]
