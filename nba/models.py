from django.db import models
from django.utils import timezone

class nba(models.Model):
    # so you can apparently access nba.ATL easier?
    
    ATL = 'ATL'
    BKN = 'BKN'
    BOS = 'BOS'
    CHA = 'CHA'
    CHI = 'CHI'
    CLE = 'CLE'
    DAL = 'DAL'
    DEN = 'DEN'
    DET = 'DET'
    GS = 'GS'
    HOU = 'HOU'
    IND = 'IND'
    LAC = 'LAC'
    LAL = 'LAL'
    MEM = 'MEM'
    MIA = 'MIA'
    MIL = 'MIL'
    MIN = 'MIN'
    NOP = 'NOP'
    NYK = 'NYK'
    OKC = 'OKC'
    ORL = 'ORL'
    PHI = 'PHI'
    PHX = 'PHX'
    POR = 'POR'
    SAC = 'SAC'
    SA = 'SA'
    TOR = 'TOR'
    UTA = 'UTA'
    WAS = 'WAS'

    
    TEAMS = (
        (ATL, 	'Atlanta Hawks'),
        (BKN, 	'Brooklyn Nets'),
        (BOS, 	'Boston Celtics'),
        (CHA, 	'Charlotte Hornets'),
        (CHI, 	'Chicago Bulls'),
        (CLE, 	'Cleveland Cavaliers'),
        (DAL, 	'Dallas Mavericks'),
        (DEN, 	'Denver Nuggets'),
        (DET, 	'Detroit Pistons'),
        (GS,	'Golden State Warriors'),
        (HOU, 	'Houston Rockets'),
        (IND, 	'Indiana Pacers'),
        (LAC, 	'Los Angeles Clippers'),
        (LAL, 	'Los Angeles Lakers'),
        (MEM, 	'Memphis Grizzlies'),
        (MIA, 	'Miami Heat'),
        (MIL, 	'Milwaukee Bucks'),
        (MIN, 	'Minnesota Timberwolves'),
        (NOP, 	'New Orleans Pelicans'),
        (NYK, 	'New York Knicks'),
        (OKC, 	'Oklahoma City Thunder'),
        (ORL, 	'Orlando Magic'),
        (PHI, 	'Philadelphia 76ers'),
        (PHX, 	'Phoenix Suns'),
        (POR, 	'Portland Trail Blazers'),
        (SAC, 	'Sacramento Kings'),
        (SA, 'San Antonio Spurs'),
        (TOR, 	'Toronto Raptors'),
        (UTA, 	'Utah Jazz'),
        (WAS, 	'Washington Wizards'),
    )
    home_Team = models.CharField(max_length=40,
                                choices=TEAMS,
                                default='Atlanta Hawks')
    home_Score = models.IntegerField(default=100)
    away_Team = models.CharField(max_length=40,
                                choices=TEAMS,
                                default='Atlanta Hawks')
    away_Score = models.IntegerField(default=100)
    date = models.DateField(default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):  
        return self.home_Team + ' vs ' + self.away_Team + ': ' + str(self.date)
# Create your models here. the name of the URL that will be used to identify the view. This can be the same as the name of the view but it can also be something
