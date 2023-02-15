from rest_framework import serializers
from .models import Level, MemberAccount, Exercise, FutureWorkout, PriorWorkout, TemplateWorkout, FutureWorkoutExercise,  PriorWorkoutExercise, TemplateExercise

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'level_id',
            'name',
        )
        model = Level

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
            'level_id',
            'description',
        )
        model = Exercise


class FutureWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'future_workout_id',
            'member_id',
            'level_id',
            'category_id',
            'name',
            'perform_on',
        )
        model = FutureWorkout        

class PriorWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'prior_workout_id',
            'member_id',
            'level_id',
            'category_id',
            'when_completed',
        )
        model = PriorWorkout


class TemplateWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'template_id',
            'member_id',
            'level_id',
            'category_id',
            'name',
        )
        model = TemplateWorkout


class TemplateExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'template_ex_id',
            'template_id',
            'exercise_id',
            'target_sets',
            'target_reps',
            'position_in_list',
        )
        model = TemplateExercise


class FutureWorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'future_workout_ex_id',
            'future_workout_id',
            'exercise_id',
            'target_sets',
            'target_reps',
            'position_in_list',
        )
        model = FutureWorkoutExercise

class PriorWorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'prior_workout_ex_id',
            'exercise_id',
            'prior_workout_id',
            'target_sets',
            'target_reps',
            'position_in_list',
        )
        model = PriorWorkoutExercise