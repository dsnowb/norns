# Generated by Django 2.0.5 on 2018-05-24 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_player_desired_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='desired_action',
            new_name='combat_action',
        ),
    ]