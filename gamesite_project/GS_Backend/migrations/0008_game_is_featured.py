# Generated by Django 4.2.7 on 2023-11-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GS_Backend', '0007_game_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
