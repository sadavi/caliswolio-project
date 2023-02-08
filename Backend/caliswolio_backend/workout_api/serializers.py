from rest_framework import serializers
from .models import Exercise, MemberAccount, FutureWorkout, PriorWorkout, PriorWorkoutExercises, TemplateExercises

# Need to fill out the rest of the models like the ones below
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'member_id',
            'email',
            'password',
            'phone_number',
            'level_id',
            'birth_year',
            'gender',
            'zipcode',
        )
        model = MemberAccount


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'exercise_id',
            'name',
            'category',
            'level',
            'description',
        )
        model = Exercise