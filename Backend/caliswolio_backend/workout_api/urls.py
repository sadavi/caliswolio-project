from django.urls import path, include
from caliswolio_backend import views

urlpatterns = [
    path('getExercises/', views.getExercises),
    path('getExercise/<int:exercise_id>/', views.getExercise),
    path('getLevels/', views.getLevels),
    path('Accounts/', views.MemberAccountList.as_view()),
    path('Account/<int:pk>/', views.MemberAccountDetail.as_view()),
    path('fwl/', views.FutureWorkoutList.as_view()),
    path('fwd/<int:pk>/', views.FutureWorkoutDetail.as_view()),
    path('fwel/', views.FutureWorkoutExerciseList.as_view()),
    path('fwed<int:pk>/', views.FutureWorkoutExerciseDetail.as_view()),
    path('pwl/<member_id>/', views.PriorWorkoutList.as_view()),
    path('pwd/<int:pk>/', views.PriorWorkoutDetail.as_view()),
    path('pwel/', views.PriorWorkoutExerciseList.as_view()),
    path('pwed/<int:pk>/', views.PriorWorkoutExerciseDetail.as_view()),
    path('twl/<member>', views.TemplateWorkoutList.as_view()),
    path('twd/<int:pk>/', views.TemplateWorkoutDetail.as_view()),
    path('tel/<member>/', views.TemplateExerciseList.as_view()),
    path('ted/<int:pk>/', views.TemplateExerciseDetail.as_view()),
]