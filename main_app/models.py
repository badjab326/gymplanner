from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Exercise(models.Model):
  name = models.CharField(max_length=50)
  sets = models.IntegerField()
  reps = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} {self.sets} {self.reps}'

  def get_absolute_url(self):
    return reverse('exercises_detail', kwargs={'pk': self.id})

class Routine(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    days_per_week = models.IntegerField()
    exercises = models.ManyToManyField(Exercise)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def done_today(self):
        return self.taking_set.filter(date=date.today()).count() >= 1

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'routine_id': self.id})

class Doing(models.Model):
    date = models.DateField('workout date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
