from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from django102.models import Game


def something(request):
    return HttpResponse('It works!')


def index(request):
    title = 'SoftUni Django 101'
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
        'app_name': 'my_first_app',
    }
    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index.html'


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'