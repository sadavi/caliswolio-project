from django.urls import path, include
from caliswolio_backend import views

urlpatterns = [
    path('getExercises/', views.getExercises),
    path('getExercise/<int:exercise_id>/', views.getExercise),
    path('getLevels/', views.getLevels),
    path('Accounts/<int:member_id>/', views.MemberAccountView.as_view()),
    path('fw/<int:future_workout_id>/', views.FutureWorkoutView.as_view()),
    path('pw/<int:prior_workout_id>/', views.PriorWorkoutView.as_view()),
    path('tw/<int:template_id>/', views.TemplateWorkoutView.as_view()),
    path('te/<int:template_ex_id>/', views.TemplateExerciseView.as_view()),
    path('fwe/<int:future_workout_ex_id>/', views.FutureWorkoutExerciseView.as_view()),
    path('pwe/<int:prior_workout_ex_id>/', views.PriorWorkoutExerciseView.as_view())
    
]
