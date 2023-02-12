from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from workout_api.models import Level, Exercise, MemberAccount
from workout_api.serializers import ExerciseSerializer, LevelSerializer, MemberAccountSerializer

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

