from django.db import models


class BallPlayer(models.Model):
    name_last = models.CharField(db_column='name_last', max_length=255, blank=True, null=True)
    name_first = models.CharField(db_column='name_first', max_length=255, blank=True, null=True)
    birth_country = models.CharField(db_column='birth_country', max_length=255, blank=True, null=True)
    birth_state = models.CharField(db_column='birth_state', max_length=255, blank=True, null=True)
    birth_city = models.CharField(db_column='birth_city', max_length=255, blank=True, null=True)
    number = models.IntegerField(null=True)
    position = models.CharField(max_length=80, null=True, default="Player Position")
    weight = models.IntegerField(db_column='weight', blank=True, null=True)
    height = models.FloatField(db_column='height', blank=True, null=True)
    bats = models.CharField(db_column='bats', max_length=255, blank=True, null=True)
    throws = models.CharField(db_column='throws', max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'BallPlayer'

class Batting(models.Model):
    player_name = models.CharField(db_column='player_name', max_length=80, default=None, blank=True, null=True)
    team_name = models.CharField(db_column='team_name', default=None, max_length=80, blank=True, null=True)
    league = models.CharField(db_column='league', max_length=80, default=None, blank=True, null=True)
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    at_bats = models.IntegerField(db_column='at_bats', blank=True, null=True)
    runs = models.IntegerField(db_column='runs', blank=True, null=True)
    hits = models.IntegerField(db_column='hits', blank=True, null=True)
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    avg = models.FloatField(db_column='avg', blank=True, null=True)
    class Meta:
        db_table = 'Batting'

class Pitching(models.Model):
    player_name = models.CharField(db_column='player_name', max_length=80, blank=True, null=True)
    team_name = models.CharField(db_column='team_name', max_length=80, blank=True, null=True)
    league = models.CharField(db_column='league', max_length=80, blank=True, null=True)
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    shutouts = models.IntegerField(db_column='shutouts', blank=True, null=True)
    saves = models.IntegerField(db_column='saves', blank=True, null=True)
    outs_pitched = models.IntegerField(db_column='outs_pitched', blank=True, null=True)
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    strikeouts = models.IntegerField(db_column='strikeouts', blank=True, null=True)
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'Pitching'

class Teams(models.Model):
    league = models.CharField(db_column='league', max_length=80, blank=True, null=True)
    team = models.CharField(db_column='team', max_length=80, blank=True, null=True)
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    home_games = models.IntegerField(db_column='home_games', blank=True, null=True)
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    at_bats = models.IntegerField(db_column='at_bats', blank=True, null=True)
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase. """
    
    class Meta:
        db_table = 'Team Data' 

class add_team(models.Model):
    school_name = models.CharField(max_length=80, null=False)
    team_name = models.CharField(max_length=80, null=False)
    city = models.CharField(max_length=80, null=False)
    state = models.CharField(max_length=80, null=False)
    class Meta:
        db_table = 'BaseballTeams'

class Players(models.Model):
    first_name = models.CharField(max_length=80, null=True)
    last_name = models.CharField(max_length=80, null=True)
    player_number = models.IntegerField(null=True)
    player_position = models.CharField(max_length=4, null=True, default="Player Position")
    team_name = models.CharField(max_length=80, null=True)
    class Meta:
        db_table = 'Players'

