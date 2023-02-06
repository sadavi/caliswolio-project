from rest_framework import serializers
from .models import Exercise, MemberAccount, FutureWorkout, FutureWorkoutExercises, PriorWorkout, PriorWorkoutExercises, TemplateExercises, TemplateWorkout

# Need to fill out the rest of the models like the ones below
class MemberAccountSerializer(serializers.ModelSerializer):
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


class FutureWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'future_workout_id',
            'level_id',
            'category_id',
            'name',
            'perform_on',
        )
        model = FutureWorkout


class FutureWorkoutExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'future_workout_ex_id',
            'future_workout_id',
            'exercise_id',
            'target_sets',
            'target_reps',
            'position_in_list',
        )
        model = FutureWorkoutExercises
        

class PriorWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'workout_id',
            'member_id',
            'level_id',
            'category_id',
            'when_completed',
        )
        model = PriorWorkout


class PriorWorkoutExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'prior_workout_ex_id',
            'exercise_id',
            'workout_id',
            'target_sets',
            'target_reps',
            'actual_sets',
            'actual_reps',
            'position_in_list',
        )
        model = PriorWorkoutExercises


class TemplateWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'template_id',
            'member_id',
            'level_id',
            'category_id',
            'name',
        )
        models = TemplateWorkout


class TemplateExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'template_ex_id',
            'template_id',
            'exercise_id',
            'target_sets',
            'target_reps',
        )
        models = TemplateExercises
