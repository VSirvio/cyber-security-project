from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Movie


def loginPageView(request):
    return render(request, 'movielistapp/login.html')

def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    auth_user = authenticate(request, username=username, password=password)
    login(request, auth_user)
    return redirect('home')

def logoutView(request):
    logout(request)
    return redirect('home')

def registerPageView(request):
    return render(request, 'movielistapp/register.html')

def registerView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    new_user = User.objects.create_user(username=username, password=password)
    new_user.save()
    auth_user = authenticate(request, username=username, password=password)
    login(request, auth_user)
    return redirect('home')

def homePageView(request):
    if request.user.is_authenticated:
        return redirect('listpage')
    return redirect('loginpage')

def listPageView(request):
    movies = Movie.objects.all()
    params = {'movies': movies, 'username': request.user.username}
    return render(request, 'movielistapp/index.html', params)

def movieAddingPageView(request):
    return render(request, 'movielistapp/add.html')

def addView(request):
    movie_title = request.POST.get('title')
    new_movie = Movie.objects.create(title=movie_title)
    new_movie.save()
    return redirect('home')
