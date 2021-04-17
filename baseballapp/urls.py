"""baseballapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from register import views as r
from allbaseball import views as h
from .views import TeamsDataChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', h.home, name='home'),
    path('home/', h.home, name='home'),
    path('players/', views.ball_player, name='players'),
    path('batting/', views.BattingData, name='batting'),
    #path('pitchingdata/', views.pitching, name='pitchingdata'),
    path('pitchers/', views.PitchingData, name='pitchers'),
    path('teamsdata/', views.TeamsData, name='teamsdata'),
    path('addteam/', views.add_teams, name='addteam'),
    path('addplayer/', views.add_player, name='addplayer'),
    path('allplayers/', views.all_players, name='allplayers'),
    path('teams/', views.team_names, name='teams'),
    path('register/', r.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('chartview/', TeamsDataChartView.as_view(), name='chartview'),
]