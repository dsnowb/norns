# Generated by Django 2.0.5 on 2018-05-24 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_auto_20180524_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Tile'),
        ),
    ]