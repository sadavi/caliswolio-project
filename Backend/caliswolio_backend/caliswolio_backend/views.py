from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view
from workout_api.models import Exercise
from workout_api.serializers import ExerciseSerializer

@api_view(['GET'])
def getExercises(request):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return response(serializer.data)