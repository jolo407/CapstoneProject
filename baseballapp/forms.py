from django import forms
from . models import add_team, Players

class AddTeamForm(forms.Form):
    school_name = forms.CharField(label='School Name', max_length=80)
    team_name = forms.CharField(label='Team Name', max_length=80)
    city_name = forms.CharField(label='City', max_length=80)
    state = forms.CharField(label='State', max_length=80)

    class Meta:
        model = add_team
        fields = ('school_name', 'team_name', 'city_name', 'state', )


class AddPlayerForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    player_number = forms.IntegerField(label='Player Number')
    player_position = forms.CharField(label='Player Position', max_length=80)
    team_name = forms.CharField(label='Team Name', max_length=80)

    class Meta:
        model = Players
        fields = ('first_name', 'last_name', 'player_number', 'player_position', )