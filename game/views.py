from django.shortcuts import render

# Create your views here.

from .models import Leaderboard
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    leaderboard = Leaderboard.objects.order_by('-points')[:10]
    context = {
        'leaderboard': leaderboard,
    }
    return render(request, 'game/index.html', context)

def log_in(request):
    try:
        username = User.objects.get(username = request.POST['name'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'game/index.html', {
            'error_message': "Invalid Username.",
        })
    else:
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username = name, password = password)
        print (request.POST['name'] + " "+ request.POST['password'])

        if user is not None:
            login(request, user)
            return render(request, 'game/index.html')
    return render(request, 'game/index.html', {
        'error_message': "Invalid Password.",
    })

def signup(request):
    try:
        username = User.objects.get(username = request.POST['username'])
    except (KeyError, User.DoesNotExist):
        if (request.POST['s_password'] == request.POST['reenterpassword']):
            user = User.objects.create_user(request.POST.get('username', False), request.POST.get('email', False), request.POST.get('password', False))
            login(request, user)
            return render(request, 'game/index.html')
    else:
        return render(request, 'game/index.html', {
            'error_message': "Username already in use",
        })
    return render(request, 'game/index.html', {
        'error_message': "Passwords don't match",
    })

def save_score(request):
    try:
        username = User.objects.get(pk = request.user.id)
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        leaderboard = Leaderboard.objects.order_by('-points')[:10]
        context = {
            'leaderboard': leaderboard,
        }
        return render(request, 'game/index.html', context)
    else:
        new_entry = Leaderboard(user = username, points = int(request.POST['score']))
        new_entry.save()
        leaderboard = Leaderboard.objects.order_by('-points')[:10]
        context = {
            'leaderboard': leaderboard,
        }
        return render(request, 'game/index.html', context)


def log_out(request):
    logout(request)
    leaderboard = Leaderboard.objects.order_by('-points')[:10]
    context = {
        'leaderboard': leaderboard,
    }
    return render(request, 'game/index.html', context)
