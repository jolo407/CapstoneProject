# Generated by Django 3.1.7 on 2021-03-30 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseballapp', '0020_players_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pitching',
            name='stint',
        ),
    ]
