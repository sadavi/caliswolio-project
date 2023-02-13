from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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
def getExercise(request, exercise_id):
    exercises = Exercise.objects.get(exercise_id=exercise_id)
    serializer = ExerciseSerializer(exercises, many=False)
    return Response(serializer.data)

@api_view(['GET'])  
def getLevels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)

@api_view(['GET'])  
def getLevel(request, level_id):
    levels = Level.objects.get(level_id=level_id)
    serializer = LevelSerializer(levels, many=False)
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
            'Template ID': request.data.get('prior_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Completed': request.data.get('when_completed'),
            'Name': request.data.get('name'),
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

class TemplateExerciseView(APIView):
    def get_object(self, template_ex_id):
        # Get the Template Exercise
        try:
            return TemplateExercise.objects.get(id=template_ex_id)
        except TemplateExercise.DoesNotExist:
            return None

    def get(self, template_ex_id):
        """
        Helper method to get the object with given template_ex_id
        """
        exercise_instance = self.get_object(template_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TemplateExerciseSerializer(exercise_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Template Exercise ID': request.data.get('template_ex_id'),
            'Template ID': request.data.get('template_id'),
            'Exercise ID': request.data.get('exercise_id'),
            'Target Sets': request.data.get('target_sets'),
            'Target Reps': request.data.get('target_reps'),
            'Position in List': request.data.get('position_in_list'),
        }
        serializer = TemplateExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, template_ex_id):
        #Update
        exercise_instance = self.get_object(template_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Template Exercise ID': request.data.get('template_ex_id'),
            'Template ID': request.data.get('template_id'),
            'Exercise ID': request.data.get('exercise_id'),
            'Target Sets': request.data.get('target_sets'),
            'Target Reps': request.data.get('target_reps'),
            'Position in List': request.data.get('position_in_list'),
        }
        serializer = TemplateExerciseSerializer(instance=exercise_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, template_ex_id):
        # Delete
        exercise_instance = self.get_object(template_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        exercise_instance.delete()
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
            'Template ID': request.data.get('prior_workout_id'),
            'Member ID': request.data.get('member_id'),
            'Level ID': request.data.get('level_id'),
            'Category ID': request.data.get('category_id'),
            'Completed': request.data.get('when_completed'),
            'Name': request.data.get('name'),
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

class FutureWorkoutExerciseView(APIView):
    def get_object(self, future_workout_ex_id):
        # Get the Future Workout Exercise
        try:
            return FutureWorkoutExercise.objects.get(id=future_workout_ex_id)
        except FutureWorkoutExercise.DoesNotExist:
            return None

    def get(self, future_workout_ex_id):
        """
        Helper method to get the object with given future_workout_ex_id
        """
        exercise_instance = self.get_object(future_workout_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FutureWorkoutExerciseSerializer(exercise_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Future Workout Exercise ID': request.data.get('future_workout_ex_id'),
            'Future Workout ID': request.data.get('future_workout_id'),
            'Exercise ID': request.data.get('exercise_id'),
            'Target Sets': request.data.get('target_sets'),
            'Target Reps': request.data.get('target_reps'),
            'Position in List': request.data.get('position_in_list'),
        }
        serializer = FutureWorkoutExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, future_workout_ex_id):
        #Update
        exercise_instance = self.get_object(future_workout_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Future Workout Exercise ID': request.data.get('future_workout_ex_id'),
            'Future Workout ID': request.data.get('future_workout_id'),
            'Exercise ID': request.data.get('exercise_id'),
            'Target Sets': request.data.get('target_sets'),
            'Target Reps': request.data.get('target_reps'),
            'Position in List': request.data.get('position_in_list'),
        }
        serializer = FutureWorkoutExerciseSerializer(instance=exercise_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, future_workout_ex_id):
        # Delete
        exercise_instance = self.get_object(future_workout_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        exercise_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )

class PriorWorkoutExerciseView(APIView):
    def get_object(self, prior_workout_ex_id):
        # Get the Prior Workout Exercise
        try:
            return PriorWorkoutExercise.objects.get(id=prior_workout_ex_id)
        except PriorWorkoutExercise.DoesNotExist:
            return None

    def get(self, prior_workout_ex_id):
        """
        Helper method to get the object with given prior_workout_ex_id
        """
        exercise_instance = self.get_object(prior_workout_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PriorWorkoutExerciseSerializer(exercise_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create
        data = {
            'Prior Workout Exercise ID': request.data.get('prior_workout_ex_id'),
            'Prior Workout ID': request.data.get('prior_workout_id'),
            'Exercise ID': request.data.get('exercise_id'),
            'Target Sets': request.data.get('target_sets'),
            'Target Reps': request.data.get('target_reps'),
            'Position in List': request.data.get('position_in_list'),
        }
        serializer = PriorWorkoutExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, prior_workout_ex_id):
        #Update
        exercise_instance = self.get_object(prior_workout_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Future Workout Exercise ID': request.data.get('future_workout_ex_id'),
            'Future Workout ID': request.data.get('future_workout_id'),
            'Exercise ID': request.data.get('exercise_id'),
            'Target Sets': request.data.get('target_sets'),
            'Target Reps': request.data.get('target_reps'),
            'Position in List': request.data.get('position_in_list'),
        }
        serializer = PriorWorkoutExerciseSerializer(instance=exercise_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, prior_workout_ex_id):
        # Delete
        exercise_instance = self.get_object(prior_workout_ex_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        exercise_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )