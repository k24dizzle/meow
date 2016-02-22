from django.shortcuts import render
from django.utils import timezone
from django.http import Http404
from .models import nba
from django.http import HttpResponse
from django.db.models import Q
def nba_list(request):
    games = nba.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'nba/nba_list.html', {'games': games})

def score(request, game_id):
    try:
        game = nba.objects.get(pk=game_id)
    except: 
       raise Http404("Game does not exist") 
    return render(request, 'nba/score.html', {'game': game})

def team(request, team):
    games = nba.objects.filter(Q(home_Team=team) | Q(away_Team=team)).filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'nba/team.html', {'games': games, 'team': team}) 

def maps(request, team):
    return render(request, 'nba/map.html', {'team': team})
# Create your views here.
