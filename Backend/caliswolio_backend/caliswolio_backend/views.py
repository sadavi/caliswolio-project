from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from workout_api.models import FutureWorkout, Level, Exercise, MemberAccount
from workout_api.serializers import *

# CREATE



# READ
@api_view(['GET'])
def getExercises(request):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLevels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMemberAccounts(request):
    members = MemberAccount.objects.all()
    serializer = MemberAccountSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFutureWorkout(request):
    fWorkout = FutureWorkout
    serializer = FutureWorkoutSerializer(fWorkout, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPriorWorkout(request):
    pWorkout = PriorWorkout
    serializer = PriorWorkoutSerializer(pWorkout, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTemplateWorkout(request):
    tWorkout = TemplateWorkout
    serializer = TemplateWorkoutSerializer(tWorkout, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTemplateExercise(request):
    tExercise = TemplateExercise
    serializer = TemplateExerciseSerializer(tExercise, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFutureWorkoutExercise(request):
    fExercise = FutureWorkoutExercise
    serializer = FutureWorkoutExerciseSerializer(fExercise, many=True)
    return Response(serializer.data)

api_view(['GET'])
def getPriorWorkoutExercise(request):
    pExercise = PriorWorkoutExercise
    serializer = PriorWorkoutExerciseSerializer(pExercise, many=True)
    return Response(serializer.data)

