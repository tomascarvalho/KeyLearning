from django.shortcuts import render

# Create your views here.

from .models import User, Leaderboard

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    leaderboard = Leaderboard.objects.order_by('-points')[:10]
    context = {
        'leaderboard': leaderboard,
    }
    return render(request, 'game/index.html', context)

def login(request):
    try:
        username = User.objects.get(name = request.POST['name'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'game/index.html', {
            'error_message': "Invalid Username.",
        })
    else:
        if (username.password == request.POST['password']):
            return render(request, 'game/index.html', {
                'userID': username.id,
            })
    return render(request, 'game/index.html', {
        'error_message': "Invalid Password.",
    })

def signup(request):
    try:
        username = User.objects.get(name = request.POST['username'])
    except (KeyError, User.DoesNotExist):
        if (request.POST['s_password'] == request.POST['reenterpassword']):
            new_user = User(name = request.POST['username'], password = request.POST['s_password'])
            new_user.save()
            return render(request, 'game/index.html', {
                'userID': new_user.id,
            })
    else:
        return render(request, 'game/index.html', {
            'error_message': "Username already in use",
        })
    return render(request, 'game/index.html', {
        'error_message': "Passwords don't match",
    })

def save_score(request):
    try:
        username = User.objects.get(pk = request.POST['id'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        leaderboard = Leaderboard.objects.order_by('-points')[:10]
        print("OH SHIT")
        a = request.POST.get("id")
        print(a)
        context = {
            'leaderboard': leaderboard,
        }
        return render(request, 'game/index.html', context)
    else:
        new_entry = Leaderboard(user = username.name, points = request.POST['score'])
        new_entry.save()
        leaderboard = Leaderboard.objects.order_by('-points')[:10]
        context = {
            'leaderboard': leaderboard,
        }
        return render(request, 'game/index.html', context)
