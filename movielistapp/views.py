import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Movie


def loginPageView(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'movielistapp/login.html')

def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    return render(request, 'movielistapp/login.html', {'error': 'Invalid username or password'})

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def registerPageView(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'movielistapp/register.html')

def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')

    username = request.POST.get('username')
    password = request.POST.get('password')

    if (not isinstance(username, str) or not isinstance(password, str) or
            len(username) < 1 or len(username) > 30 or
            len(password) < 1 or len(password) > 30 or
            re.fullmatch(r'\w*', username) is None or
            re.fullmatch(r'\w*', password) is None):
        return render(
            request,
            'movielistapp/register.html',
            {'error': 'Username and password should consist of 1-30 alphanumeric characters'}
        )

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
    if not request.user.is_authenticated:
        return redirect('loginpage')
    movies = Movie.objects.all()
    params = {'movies': movies, 'username': request.user.username}
    return render(request, 'movielistapp/index.html', params)

def movieAddingPageView(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    return render(request, 'movielistapp/add.html')

def addView(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')

    movie_title = request.POST.get('title')
    if (not isinstance(movie_title, str) or
            len(movie_title) < 1 or len(movie_title) > 100):
        return render(
            request,
            'movielistapp/add.html',
            {'error': 'Movie title should be 1-100 characters'}
        )

    new_movie = Movie.objects.create(title=movie_title)
    new_movie.save()
    return redirect('home')
