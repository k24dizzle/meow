from django.test import TestCase
from nba.models import nba
from django.utils import timezone
import datetime

def create_game(home, away, hscore, ascore, date):
    return nba.objects.create(home_Team=home, away_Team=away, home_Score=hscore, away_Score=ascore, date=date)

class nbaTestCase(TestCase):
    def testFuture(self):
        now = timezone.now().date()
        game = create_game("ATL", "BOS", 102, 133, now + datetime.timedelta(days=30))
        self.assertEqual(game.inFuture(), False)

    def testDate(self):
        game = create_game("ATL", "BOS", 102, 100, datetime.date(2016, 2, 23))
        self.assertEqual(game.date, datetime.date(2016, 2, 23)) 


       
