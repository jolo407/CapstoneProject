# Generated by Django 3.1.7 on 2021-03-30 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseballapp', '0013_auto_20210330_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='year',
        ),
    ]
