# Generated by Django 4.0.6 on 2022-07-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_routine_user_exercise_doing_routine_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doing',
            name='date',
            field=models.DateField(verbose_name='Workout Date'),
        ),
    ]
