from django.http import HttpResponse
from django.shortcuts import render
from .models import Player

def index(request):
    players = Player.objects.all()
    return render(request, 'base.html', {'players': players})

