from django.contrib import admin
from .models import Level, MemberAccount, Exercise, FutureWorkout, PriorWorkout, TemplateWorkout, FutureWorkoutExercise, PriorWorkoutExercise, TemplateExercise

admin.site.register(Level)
admin.site.register(MemberAccount)
admin.site.register(Exercise)
admin.site.register(FutureWorkout)
admin.site.register(PriorWorkout)
admin.site.register(TemplateWorkout)
admin.site.register(FutureWorkoutExercise)
admin.site.register(PriorWorkoutExercise)
admin.site.register(TemplateExercise)