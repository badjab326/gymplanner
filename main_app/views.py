from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Routine, Exercise
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DoingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')

@login_required
def routines_index(request):
  routines = Routine.objects.filter(user=request.user)
  return render(request, 'routines/index.html', { 'routines': routines })

@login_required
def routines_detail(request, routine_id):
  routine = Routine.objects.get(id=routine_id)
  doing_form = DoingForm()
  exercises_not_included = Exercise.objects.filter(user=request.user).exclude(id__in = routine.exercises.all().values_list('id'))
  return render(request, 'routines/detail.html', {
    'routine': routine, 'doing_form': doing_form,
    'exercises': exercises_not_included
   })
  
@login_required
def exercises_index(request):
  exercises = Exercise.objects.filter(user=request.user)
  return render(request, 'exercises/index.html', {'exercises': exercises})  

@login_required
def add_doing(request, routine_id):
  form = DoingForm(request.POST)
  if form.is_valid():
    new_doing = form.save(commit=False)
    new_doing.routine_id = routine_id
    new_doing.save()
  return redirect('detail', routine_id=routine_id)

@login_required
def assoc_exercise(request, routine_id, exercise_id):
  Routine.objects.get(id=routine_id).exercises.add(exercise_id)
  return redirect('detail', routine_id=routine_id)

@login_required
def assoc_exercise_delete(request, routine_id, exercise_id):
  Routine.objects.get(id=routine_id).exercises.remove(exercise_id)
  return redirect('detail', routine_id=routine_id)

class RoutineCreate(CreateView):
  model = Routine
  fields = ['name', 'muscle_group', 'description', 'days_per_week']
  success_url = '/routines/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RoutineUpdate(LoginRequiredMixin, UpdateView):
  model = Routine
  fields = '__all__'

class RoutineDelete(LoginRequiredMixin, DeleteView):
  model = Routine
  success_url = '/routines/'

class ExerciseDetail(LoginRequiredMixin, DetailView):
  model = Exercise
  template_name = 'exercises/detail.html'

class ExerciseCreate(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ['name', 'sets', 'reps', 'startingWeight', 'endingWeight']
    success_url = '/exercises/'
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class ExerciseUpdate(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ['name', 'sets', 'reps', 'startingWeight', 'endingWeight']

class ExerciseDelete(LoginRequiredMixin, DeleteView):
    model = Exercise
    success_url = '/exercises/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid info - please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)