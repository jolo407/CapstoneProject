# Generated by Django 3.1.7 on 2021-03-31 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseballapp', '0024_auto_20210331_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batting',
            name='stint',
        ),
        migrations.RemoveField(
            model_name='batting',
            name='year',
        ),
    ]
