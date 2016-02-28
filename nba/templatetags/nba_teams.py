from django import template
register = template.Library()

#$ def (value, arg):
# var|foo:"bar"    var is the variable/value, bar is the arg
@register.filter(name='streakBoo')
def streakBoo(value):
    if (value[0] == 'W'):
        return True
    else:
        return False

@register.filter(name='win')
def win(value, args):
    if (value > args):
        return True
    else: 
        return False 
        
@register.filter(name='getAddress')
def getAddress(value):
    dict  = { 
    "ATL": '1 Philips Dr. Atlanta, GA 30303',
    "BKN": '620 Atlantic Ave, Brooklyn, NY 11217',
    "BOS": '100 Legends Way, Boston, MA 02114',
    "CHA": '333 E Trade St, Charlotte, NC 28202',
    "CHI": '1901 W Madison St, Chicago, IL 60612',
    "CLE": '1 Center Ct, Cleveland, OH 44115',
    "DAL": '2500 Victory TemplateSyntaxError atCould not parse the remainder: Ave, Dallas, TX 75219',
    "DEN": '1000 Chopper Cir, Denver, CO 80204',
    "DET": '6 Championship Dr, Auburn Hills, MI 48326',
    "GS": '7000 Coliseum Way, Oakland, CA 94621',
    "HOU": '1510 Polk St, Houston, TX 77002',
    "IND": '125 S Pennsylvania St, Indianapolis, IN 46204',
    "LAC": '1111 S Figueroa St, Los Angeles, CA 90015',
    "LAL": '1111 S Figueroa St, Los Angeles, CA 90015',
    "MEM": '191 Beale St, Memphis, TN 38103',
    "MIA": '601 Biscayne Blvd, Miami, FL 33132',
    "MIL": '1001 N 4th St, Milwaukee, WI 53203',
    "MIN": '600 First Avenue North, Minneapolis, MN 55403',
    "NOP": '1501 Dave Dixon Dr, New Orleans, LA 70113',
    "NYK": '4 Pennsylvania Plaza, New York, NY 10001',
    "OKC": '100 W Reno Ave, Oklahoma City, OK 73102',
    "ORL": '400 W Church St #200, Orlando, FL 32801',
    "PHI": '3601 S Broad St, Philadelphia, PA 19148',
    "PHX": '201 E Jefferson St, Phoenix, AZ 85004',
    "POR": '1 N Center Ct St, Portland, OR 97227',
    "SAC": '1 Sports Pkwy, Sacramento, CA 95834',
    "SA": '1 AT&T Center, San Antonio, TX 78219',
    "TOR": '40 Bay Street Toronto, Ontario, Canada',
    "UTA": '301 W South Temple, Salt Lake City, UT 84101',
    "WAS": '601 F St Nw, Washington, DC 20004',
    }
    return dict[value]

@register.filter(name='teamName')
def teamName(value):
    dict = { 
    "ATL": 'Atlanta Hawks',
    "BKN": 'Brooklyn Nets',
    "BOS": 'Boston Celtics',
    "CHA": 'Charlotte Hornets',
    "CHI": 'Chicago Bulls',
    "CLE": 'Cleveland Cavaliers',
    "DAL": 'Dallas Mavericks',
    "DEN": 'Denver Nuggets',
    "DET": 'Detriot Pistons',
    "GS": 'Golden State Warriors',
    "HOU": 'Houston Rockets',
    "IND": 'Indiana Pacers',
    "LAC": 'LA Clippers',
    "LAL": 'LA Lakers',
    "MEM": 'Memphis Grizzlies',
    "MIA": 'Miami Heat',
    "MIL": 'Milwaukee Bucks',
    "MIN": 'Minnesota Timberwolves',
    "NOP": 'New Orleans Pelicans',
    "NYK": 'New York Knicks',
    "OKC": 'Oklahoma City Thunder',
    "ORL": 'Orlando Magic',
    "PHI": 'Philadelphia 76ers',
    "PHX": 'Phoenix Suns',
    "POR": 'Portland TrailBlazers',
    "SAC": 'Sacramento Kings',
    "SA": 'San Antonio Spurs',
    "TOR": 'Toronto Raptors',
    "UTA": 'Utah Jazz',
    "WAS": 'Washington Wizards',
    }
    return dict[value]

