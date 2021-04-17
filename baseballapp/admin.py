from django.contrib import admin
from .models import BallPlayer, Batting, Pitching, Teams, add_team, Players

admin.site.register(BallPlayer)
admin.site.register(Batting)
admin.site.register(Pitching)
admin.site.register(Teams)
admin.site.register(add_team)
admin.site.register(Players)