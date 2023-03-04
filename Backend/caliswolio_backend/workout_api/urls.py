from django.urls import path, include
from caliswolio_backend import views

urlpatterns = [
    path('getExercises/', views.getExercises),
    path('getExercise/<int:exercise_id>/', views.getExercise),
    path('getLevels/', views.getLevels),
    path('Accounts/', views.MemberAccountList.as_view()),
    path('Account/<int:pk>/', views.MemberAccountDetail.as_view()),
<<<<<<< HEAD
=======
    path('fwl/', views.FutureWorkoutList.as_view()),
>>>>>>> 28d0a8522ec3664ebaf7f6b4f87f0080c8fd2a89
    path('fwl/<member_id>/', views.FutureWorkoutList.as_view()),
    path('fwd/<int:pk>/', views.FutureWorkoutDetail.as_view()),
    path('fwel/', views.FutureWorkoutExerciseList.as_view()),
    path('fwed<int:pk>/', views.FutureWorkoutExerciseDetail.as_view()),
    # path('pwl/', views.PriorWorkoutList.as_view()),
    path('pwl/<member_id>/', views.PriorWorkoutList.as_view()),
    path('pwd/<int:pk>/', views.PriorWorkoutDetail.as_view()),
    path('pwel/', views.PriorWorkoutExerciseList.as_view()),
    path('pwed/<int:pk>/', views.PriorWorkoutExerciseDetail.as_view()),
<<<<<<< HEAD
=======
    path('twl/', views.TemplateWorkoutList.as_view()),
>>>>>>> 28d0a8522ec3664ebaf7f6b4f87f0080c8fd2a89
    path('twl/<member_id>/', views.TemplateWorkoutList.as_view()),
    path('twd/<int:pk>/', views.TemplateWorkoutDetail.as_view()),
    path('tel/', views.TemplateExerciseList.as_view()),
    path('ted/<int:pk>/', views.TemplateExerciseDetail.as_view()),
]