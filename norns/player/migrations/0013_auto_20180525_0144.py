# Generated by Django 2.0.5 on 2018-05-25 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0012_merge_20180524_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='max_health',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='player',
            name='health',
            field=models.IntegerField(default=200),
        ),
    ]
