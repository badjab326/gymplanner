from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('routines/', views.routines_index, name='index'),
    path('routines/<int:routine_id>/', views.routines_detail, name='detail'),
    path('routines/create/', views.RoutineCreate.as_view(), name='routines_create'),
    path('routines/<int:pk>/update/', views.RoutineUpdate.as_view(), name='routines_update'),
    path('routines/<int:pk>/delete/', views.RoutineDelete.as_view(), name='routines_delete'),
    path('routines/<int:routine_id>/add_doing/', views.add_doing, name='add_doing'),
    path('routines/<int:routine_id>/assoc_exercise/<int:exercise_id>/', views.assoc_exercise, name='assoc_exercise'),
    path('routines/<int:routine_id>/assoc_exercise/<int:exercise_id>/delete/', views.assoc_exercise_delete, name='assoc_exercise_delete'),
    path('exercises/', views.exercises_index, name='exercises_index'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]