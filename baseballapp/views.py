from django.shortcuts import render, redirect
from baseballapp.models import BallPlayer, Batting, Pitching, add_team, Players, Teams
from .forms import AddTeamForm, AddPlayerForm
from django.views.generic import TemplateView



def ball_player(request):
    results = BallPlayer.objects.all()
    return render(request, 'ballplayer.html',{'data': results})

def BattingData(request):
    if request.method == "POST":
        batter = request.POST.get('batter', False)
        if batter == False:
            return render(request, 'battingdata.html')
        else:
            results = Batting.objects.get(pk=batter)
            return render(request, 'battingdata.html', context={'batting': results})
    else:
        return render(request, 'battingdata.html')
    #results = Batting.objects.all()
    #return render (request, 'battingdata.html', {'batting': results})

#def pitching(request, pitching_id):
    #try:
        #results = Pitching.objects.get(pk=pitching_id)
    #except Pitching.DoesNotExist:
            #raise Http404('Pitcher does not exist')

    #return render(request, 'pitchingdata.html', context={'pitching': results})

    #results = Pitching.objects.all()
    #return render(request, 'pitchingdata.html', {'pitching': results})

def PitchingData(request):
    if request.method == "POST":
        playerselect = request.POST.get('pitcher', False)
        if playerselect == False:

            return render(request, 'pitchingdata.html')
        else:
            results = Pitching.objects.get(pk=playerselect)
            return render(request, 'pitchingdata.html', context={'pitching': results})
    else:
        return render(request, 'pitchingdata.html')


def TeamsData(request):
    if request.method == "POST":
        teamsselect = request.POST.get('teamsdata', False)
        if teamsselect == False:
            return render(request, 'teamsdata.html')
        else:
            results = Teams.objects.get(pk=teamsselect)
            return render(request, 'teamsdata.html', context={'teamsdata': results}) 
    else: 
        return render(request, 'teamsdata.html')
    #results = Teams.objects.all()
    #return render(request, 'teamsdata.html', {'teams': results})

def team_names(request):
    results = add_team.objects.all()
    return render(request, 'all_teams.html', {'baseballteams': results})

def all_players(request):
    results = Players.objects.all()
    return render(request, 'all_players.html', {'players': results})


def add_teams(response):
    if response.method == "POST":
        form = AddTeamForm(response.POST)
        if form.is_valid():
            return HttpResonseRedirect("")
    else:
        form = AddTeamForm()
    
    return render(response, "add_team.html", {"form":form})

def update(request, id):
    player = Players.objects.get(id=id)
    form = AddPlayerForm(request.POST, instance = player)
    if form.is_valid():
        form.save()
        return redirect('allplayers/')
    return render(request, 'update.html', {'player': player})


def add_player(response):
    if response.method == "POST":
        form = AddPlayerForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('allplayers')
    else:
        form = AddPlayerForm()
        
    return render(response, "add_player.html", {"form":form})

class TeamsDataChartView(TemplateView):
    template_name = 'chart_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Teams.objects.all()
        return context


