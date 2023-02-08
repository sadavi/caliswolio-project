from django.contrib import admin
from .models import MemberAccount, FutureWorkout, PriorWorkout, PriorWorkoutExercises, TemplateExercises

admin.site.register(MemberAccount)
admin.site.register(FutureWorkout)
admin.site.register(PriorWorkout)
admin.site.register(PriorWorkoutExercises)
admin.site.register(TemplateExercises)