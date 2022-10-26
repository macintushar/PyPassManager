from django.db import models
from datetime import datetime
from django.utils import timezone

TECH = 'TECH'
NONE = 'NONE'
BIZ = 'BIZ'
EMAIL = 'EMAIL'
ENT = 'ENT'
FIN = 'FIN'
GAMES = 'GAMES'
NEWS = 'NEWS'
OTHER = 'OTHER'
SHOP = 'SHOP'
SOCIAL = 'SOCIAL'
SPORTS = 'SPORTS'
TECH = 'TECH'
TRAVEL = 'TRAVEL'
UTIL = 'UTIL'

CATEGORIES = (
    (TECH,'Technology'),
    (NONE,'No category'),
    (BIZ,'Business'),
    (EMAIL,'Email'), 
    (ENT,'Entertainment'),
    (FIN,'Finance'),
    (GAMES,'Games'),
    (NEWS,'News'),
    (OTHER,'Other'),
    (SHOP,'Shopping'),
    (SOCIAL,'Social media'),
    (SPORTS,'Sports'),
    (TECH,'Tech'),
    (TRAVEL,'Travel'),
    (UTIL,'Utilities'),
)

class Passwords(models.Model):
    
    app_name = models.CharField(max_length=100)
    url = models.URLField()

    username = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)

    category = models.CharField(choices=CATEGORIES,default='No Category',max_length=100)






