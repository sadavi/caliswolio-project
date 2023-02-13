from django.urls import path, include
from caliswolio_backend import views

urlpatterns = [
    path('getExercises', views.getExercises),
    path('getExercise/<int:exercise_id>/', views.getExercise),
    path('getLevels', views.getLevels),
    path('Accounts', views.MemberAccountView.as_view()),
]