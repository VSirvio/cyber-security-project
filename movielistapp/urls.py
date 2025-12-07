from django.urls import path

from .views import (
    homePageView,
    registerPageView,
    registerView,
    loginPageView,
    loginView,
    listPageView,
    movieAddingPageView,
    addView,
)

urlpatterns = [
    path('', homePageView, name='home'),
    path('registerpage/', registerPageView, name='registerpage'),
    path('register/', registerView, name='register'),
    path('loginpage/', loginPageView, name='loginpage'),
    path('login/', loginView, name='login'),
    path('listpage/', listPageView, name='listpage'),
    path('addingpage/', movieAddingPageView, name='addingpage'),
    path('add/', addView, name='add'),
]
