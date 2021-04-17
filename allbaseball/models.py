from django.db import models


"""
class Batting(models.Model):
    player_id = models.CharField(db_column='player_id', max_length=9, blank=True, null=True)
    year_id = models.SmallIntegerField(db_column='year_id', blank=True, null=True)
    stint = models.SmallIntegerField(db_column='stint', blank=True, null=True)
    team_id = models.CharField(db_column='team_id', max_length=3, blank=True, null=True)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
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


class BallPlayer(models.Model):
    player_id = models.CharField(db_column='player_id', primary_key=True, max_length=255)
    birth_country = models.CharField(db_column='birth_country', max_length=255, blank=True, null=True)
    birth_state = models.CharField(db_column='birth_state', max_length=255, blank=True, null=True)
    birth_city = models.CharField(db_column='birth_city', max_length=255, blank=True, null=True)
    name_first = models.CharField(db_column='name_first', max_length=255, blank=True, null=True)
    name_last = models.CharField(db_column='name_last', max_length=255, blank=True, null=True)
    player_number = models.IntegerField(null=True)
    player_pos = models.CharField(max_length=80, null=True, default="Player Position")
    weight = models.IntegerField(db_column='weight', blank=True, null=True)
    height = models.IntegerField(db_column='height', blank=True, null=True)
    bats = models.CharField(db_column='bats', max_length=255, blank=True, null=True)
    throws = models.CharField(db_column='throws', max_length=255, blank=True, null=True)


class Pitching(models.Model):
    player_id = models.CharField(db_column='player_id', max_length=9, blank=True, null=True)
    year_id = models.IntegerField(db_column='year_id', blank=True, null=True)
    stint = models.IntegerField(db_column='stint', blank=True, null=True)
    team_id = models.CharField(db_column='team_id', max_length=3, blank=True, null=True)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
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


class Teams(models.Model):
    year_id = models.IntegerField(db_column='year_id', primary_key=True)
    league_id = models.CharField(db_column='league_id', max_length=2, blank=True, null=True)
    team_id = models.CharField(db_column='team_id', max_length=3)
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







