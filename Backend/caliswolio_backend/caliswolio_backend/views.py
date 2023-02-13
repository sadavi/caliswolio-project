from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from workout_api.models import *
from workout_api.serializers import *


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
    members = MemberAccounts.objects.all()
    serializer = MemberAccountSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMemberAccount(request, member_id):
    member = MemberAccounts.objects.get(id=member_id)
    serializer = MemberAccountSerializer(member, many=False)
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



class MemberAccountView(APIView):
    def get_object(self, member_id):
        # Get the member account
        try:
            return MemberAccount.objects.get(id=member_id)
        except MemberAccount.DoesNotExist:
            return None

    def get(self, member_id):
        """
        Helper method to get the object with given member_id
        """
        member_instance = self.get_object(member_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(project_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Email': request.data.get('email'),
            'Password': request.data.get('password'),
            'Phone Number': request.data.get('phone_number'),
            'Birth Year': request.data.get('birth_year'),
            'Gender': request.data.get('gender'),
            'Zipcode': request.data.get('zipcode'),
            'Level': request.data.get('level_id'),
        }
        serializer = MemberAccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, member_id):
        #Update
        member_instance = getMemberAccount(request)
        if not member_instance:
            return Response(
                {"res": "Object with member id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Email': request.data.get('email'),
            'Password': request.data.get('password'),
            'Phone Number': request.data.get('phone_number'),
            'Birth Year': request.data.get('birth_year'),
            'Gender': request.data.get('gender'),
            'Zipcode': request.data.get('zipcode'),
            'Level': request.data.get('level_id'),
        }
        serializer = MemberAccountSerializer(instance=member_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, member_id):
        # Delete
        member_instance = self.get_object(member_id)
        if not member_instance:
            return Response(
                {"res": "Object with member id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        member_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )