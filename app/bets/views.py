from django.http import HttpResponse
from django.shortcuts import render
from .models import Player
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    players = Player.objects.all()
    return render(request, 'base.html', {'players': players})


@csrf_protect
def update_shotguns_owed(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "increment":
            player.shotguns_owed += 1
        elif action == "decrement" and player.shotguns_owed > 0:
            player.shotguns_owed -= 1
        player.save()
    return redirect(request.META.get("HTTP_REFERER", "/"))