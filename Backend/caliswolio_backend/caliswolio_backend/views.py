from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics
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


class MemberAccountList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MemberAccount.objects.all()
    serializer_class = MemberAccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MemberAccountDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = MemberAccount.objects.all()
    serializer_class = MemberAccountSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FutureWorkoutList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = FutureWorkout.objects.all()
    serializer_class = FutureWorkoutSerializer

    def get_queryset(self):
        member = self.kwargs['member_id']
        return PriorWorkout.objects.filter(member_id=member)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FutureWorkoutDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = FutureWorkout.objects.all()
    serializer_class = FutureWorkoutSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FutureWorkoutExerciseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = FutureWorkoutExercise.objects.all()
    serializer_class = FutureWorkoutExerciseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FutureWorkoutExerciseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = FutureWorkoutExercise.objects.all()
    serializer_class = FutureWorkoutExerciseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PriorWorkoutList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PriorWorkout.objects.all()
    serializer_class = PriorWorkoutSerializer

    def get_queryset(self):
        member = self.kwargs['member_id']
        return PriorWorkout.objects.filter(member_id=member)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PriorWorkoutDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = PriorWorkout.objects.all()
    serializer_class = PriorWorkoutSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PriorWorkoutExerciseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PriorWorkout.objects.all()
    serializer_class = PriorWorkoutSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PriorWorkoutExerciseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = PriorWorkoutExercise.objects.all()
    serializer_class = PriorWorkoutExerciseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TemplateWorkoutList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TemplateWorkout.objects.all()
    serializer_class = TemplateWorkoutSerializer

    def get_queryset(self):
        member = self.kwargs['member_id']
        return PriorWorkout.objects.filter(member_id=member)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TemplateWorkoutDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = TemplateWorkout.objects.all()
    serializer_class = TemplateWorkoutSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TemplateExerciseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TemplateExercise.objects.all()
    serializer_class = TemplateExerciseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TemplateExerciseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = TemplateExercise.objects.all()
    serializer_class = TemplateExerciseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)