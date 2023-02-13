from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from workout_api.models import *
from workout_api.serializers import *

# READ
@api_view(['GET'])  #  We may be able to keep as is due to us just needing a get command
def getExercises(request):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)

@api_view(['GET'])  #  We may be able to keep as is due to us just needing a get command
def getExercise(request, exercise_id):
    exercises = Exercise.objects.get(id=exercise_id)
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)

@api_view(['GET'])  #  We may be able to keep as is due to us just needing a get command
def getLevels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
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
        if not member_instance:
            return Response(
                {"res": "Object with member id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MemberAccountSerializer(member_instance)
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
        member_instance = self.get_object(member_id)
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


class FutureWorkoutView(APIView):
    def get_object(self, future_workout_id):
        # Get the Future Workout
        try:
            return FutureWorkout.objects.get(id=future_workout_id)
        except FutureWorkout.DoesNotExist:
            return None

    def get(self, future_workout_id):
        """
        Helper method to get the object with given future_workout_id
        """
        workout_instance = self.get_object(future_workout_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FutureWorkoutSerializer(workout_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Future Workout ID': request.data.get('future_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Name': request.data.get('name'),
            'Perform on': request.data.get('perform_on'),
        }
        serializer = FutureWorkoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, future_workout_id):
        #Update
        workout_instance = self.get_object(future_workout_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Future Workout ID': request.data.get('future_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Name': request.data.get('name'),
            'Perform on': request.data.get('perform_on'),
        }
        serializer = FutureWorkoutSerializer(instance=workout_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, future_workout_id):
        # Delete
        workout_instance = self.get_object(future_workout_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        workout_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )


class PriorWorkoutView(APIView):
    def get_object(self, prior_workout_id):
        # Get the Prior Workout
        try:
            return PriorWorkout.objects.get(id=prior_workout_id)
        except PriorWorkout.DoesNotExist:
            return None

    def get(self, prior_workout_id):
        """
        Helper method to get the object with given prior_workout_id
        """
        workout_instance = self.get_object(prior_workout_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PriorWorkoutSerializer(workout_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Prior Workout ID': request.data.get('prior_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Completed': request.data.get('when_completed'),
        }
        serializer = PriorWorkoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, prior_workout_id):
        #Update
        workout_instance = self.get_object(prior_workout_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Prior Workout ID': request.data.get('prior_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Completed': request.data.get('when_completed'),
        }
        serializer = PriorWorkoutSerializer(instance=workout_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, prior_workout_id):
        # Delete
        workout_instance = self.get_object(prior_workout_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        workout_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )


class TemplateWorkoutView(APIView):
    def get_object(self, template_id):
        # Get the Template Workout
        try:
            return TemplateWorkout.objects.get(id=template_id)
        except TemplateWorkout.DoesNotExist:
            return None

    def get(self, template_id):
        """
        Helper method to get the object with given template_id
        """
        workout_instance = self.get_object(template_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TemplateWorkoutSerializer(workout_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Prior Workout ID': request.data.get('prior_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Completed': request.data.get('when_completed'),
        }
        serializer = TemplateWorkoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, template_id):
        #Update
        workout_instance = self.get_object(template_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Template ID': request.data.get('template_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Name': request.data.get('name'),
        }
        serializer = TemplateWorkoutSerializer(instance=workout_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, template_id):
        # Delete
        workout_instance = self.get_object(template_id)
        if not workout_instance:
            return Response(
                {"res": "Object with workout id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        workout_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )