from django.shortcuts import render

# Create your views here.

from .models import Leaderboard, Scenarios, Scenario_Completed_By
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    active_scenarios = Scenarios.objects.filter(active = True)
    leaderboard = Leaderboard.objects.order_by('-points')[:10]
    if request.user.is_authenticated():
        completed = Scenario_Completed_By.objects.filter(user = User.objects.get(pk = request.user.id))
    else:
        completed = None
    context = {
        'leaderboard': leaderboard,
        'scenarios': active_scenarios,
        'completed': completed,
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

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/game/')

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
            return HttpResponseRedirect('/game/')
    else:
        return render(request, 'game/index.html', {
            'error_message': "Username already in use",
        })
    return render(request, 'game/index.html', {
        'error_message': "Passwords don't match",
    })

@login_required
def save_score(request):
    try:
        username = User.objects.get(pk = request.user.id)
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponseRedirect('/game/')
    else:
        new_entry = Leaderboard(user = username, points = int(request.POST['score']))
        new_entry.save()
        return HttpResponseRedirect('/game/')

@login_required
def save_notes(request):
    notes = request.POST['notes']
    creator = request.POST['creator']
    new_entry = Scenarios(notes = notes, creator = creator)
    new_entry.save()
    return HttpResponseRedirect('/game/')

@login_required
def save_success(request):
    user_id = request.POST['id']
    success = int(request.POST['success'])
    scen_id = int(request.POST['scen_id'])
    if (success):
        try:
            user = User.objects.get(pk = request.user.id)
        except (KeyError, User.DoesNotExist):
            # Redisplay the question voting form.
            return HttpResponseRedirect('/game/')
        else:
            try:
                scenario = Scenarios.objects.get(pk = scen_id)
            except (KeyError, Scenarios.DoesNotExist):
                return HttpResponseRedirect('/game/')
            else:
                new_entry = Scenario_Completed_By(user = user, scenario = scenario)
                new_entry.save()
                return HttpResponseRedirect('/game/')
    return HttpResponseRedirect('/game/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/game/')
