# Generated by Django 3.1.7 on 2021-03-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseballapp', '0016_remove_teams_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='year',
            field=models.CharField(blank=True, db_column='year', max_length=80, null=True),
        ),
    ]
