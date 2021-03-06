from django.shortcuts import render
from django.utils import timezone
from django.http import Http404
from .models import nba
from django.http import HttpResponse
from django.db.models import Q
from .templatetags import nba_teams

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
    try:
        nba_teams.teamName(team)
    except:
        raise Http404("Team does not exist: " + team)
    games2 = nba.objects.filter(Q(home_Team=team) | Q(away_Team=team)).filter(date__lte=timezone.now()).order_by('-date')
    test = calcRecord(games2, team)
    winStreak = formatStreak(calcStreak(games2, team))
    eff = calcEff(games2, team)
    return render(request, 'nba/team.html', {'games': games2, 'team': team, 'wins': test[0], 'losses': test[1], 'streak': winStreak, 'offEff': eff[0], 'defEff': eff[1]}) 

def maps(request, team):
    return render(request, 'nba/map.html', {'team': nba_teams.teamName(team), 'address': nba_teams.getAddress(team)})


#calculates a team's record based on "games" and the teams name (to help identify if
# they won or lost)
def calcRecord(games, team):
    win = 0;
    loss = 0;
    for game in games:
        if (game.home_Team == team):
            if game.home_Score > game.away_Score:
                win += 1
            else: 
                loss += 1
        else:    

            if game.away_Score > game.home_Score:
                win += 1
            else:
                loss += 1
    return [win, loss]

def calcStreak(games, team):
    streak = 0;
    for game in games:
        if(game.home_Team == team):
            if game.home_Score > game.away_Score:
                if (streak < 0):
                    return streak
                else: 
                    streak += 1
            else:
                if (streak > 0):
                    return streak
                else:
                    streak -= 1
        else:
            if game.away_Score > game.home_Score:
                if streak < 0:
                    return streak
                else: 
                    streak += 1
            else:
                if streak > 0:
                    return streak
                else:
                    streak -= 1
    return streak

def formatStreak(streak):
    if (streak < 0):
        return "Lost " + str(streak * -1)
    else:
        return "Won " + str(streak)

def calcEff(games, team):
    total = len(games)
    offense = 0
    defense = 0
    for game in games:
        if game.home_Team == team:
            offense += game.home_Score
            defense += game.away_Score
        else:
            offense += game.away_Score
            defense += game.home_Score
    return ['{0:.2f}'.format(offense/total), '{0:.2f}'.format(defense/total)]
