# Hey so I was able to get Django to auto populate some of this but there are things we may want to manually to clean up:
#   * Rearrange models' order
#   * Make sure each ForeignKey and OneToOneField has `on_delete` if it is needed
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Exercise(models.Model):
    exercise_id = models.AutoField(db_column='Exercise_ID', primary_key=True, blank=True, null=False)
    name = models.TextField(db_column='Name')
    category = models.TextField(db_column='Category')
    level = models.TextField(db_column='Level')
    description = models.TextField(db_column='Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Exercise'


class FutureWorkout(models.Model):
    future_workout_id = models.AutoField(db_column='Future_Workout_ID', primary_key=True, blank=True, null=False)
    member = models.ForeignKey('MemberAccount', models.DO_NOTHING, db_column='Member_ID')
    level = models.ForeignKey('Exercise', models.DO_NOTHING, related_name='future_level', db_column='Level')
    category = models.ForeignKey('Exercise', models.DO_NOTHING, related_name='future_cat', db_column='Category')
    name = models.TextField(db_column='Name')
    perform_on = models.DateField(db_column='Perform_On')

    class Meta:
        db_table = 'Future_Workout'


class FutureWorkoutExercises(models.Model):
    future_workout_ex_id = models.AutoField(db_column='Future_Workout_Ex_ID', primary_key=True, blank=True, null=False)
    future_workout = models.ForeignKey('FutureWorkout', models.DO_NOTHING, db_column='Future_Workout_ID')
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets', blank=True, null=True)
    target_reps = models.IntegerField(db_column='Target_Reps', blank=True, null=True)
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        managed = False
        db_table = 'Future_Workout_Exercises'


class MemberAccount(models.Model):
    member_id = models.AutoField(db_column='Member_ID', primary_key=True, blank=True, null=False)
    email = models.TextField(db_column='Email')
    password = models.TextField(db_column='Password')
    phone_number = models.TextField(db_column='Phone_Number')
    level_id = models.IntegerField(db_column='Level_ID')
    birth_year = models.IntegerField(db_column='Birth_Year')
    gender = models.TextField(db_column='Gender')
    zipcode = models.IntegerField(db_column='Zipcode')

    class Meta:
        managed = False
        db_table = 'Member_account'


class PriorWorkout(models.Model):
    workout_id = models.AutoField(db_column='Workout_ID', primary_key=True, blank=True, null=False)
    member = models.ForeignKey('MemberAccount', models.DO_NOTHING, db_column='Member_ID')
    level = models.ForeignKey('Exercise', models.DO_NOTHING, related_name= 'pri_level', db_column='Level')
    category = models.ForeignKey('Exercise', models.DO_NOTHING, related_name= 'pri_cat', db_column='Category')
    when_completed = models.DateField(db_column='When_Completed')

    class Meta:
        db_table = 'Prior_Workout'


class PriorWorkoutExercises(models.Model):
    prior_workout_ex_id = models.AutoField(db_column='Prior_Workout_Ex_ID', primary_key=True, blank=True, null=False)
    exercise_id = models.ForeignKey('Exercise', models.DO_NOTHING, db_column='Exercise_ID')
    workout = models.ForeignKey('PriorWorkout', models.DO_NOTHING, db_column='Workout_ID')
    target_sets = models.IntegerField(db_column='Target_Sets', blank=True, null=True)
    target_reps = models.IntegerField(db_column='Target_Reps', blank=True, null=True)
    actual_sets = models.IntegerField(db_column='Actual_Sets', blank=True, null=True)
    actual_reps = models.IntegerField(db_column='Actual_Reps', blank=True, null=True)
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        managed = False
        db_table = 'Prior_Workout_Exercises'


class TemplateExercises(models.Model):
    template_ex_id = models.AutoField(db_column='Template_Ex_ID', primary_key=True, blank=True, null=False)
    template = models.ForeignKey('TemplateWorkout', models.DO_NOTHING, db_column='Template_ID')
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets', blank=True, null=True)
    target_reps = models.IntegerField(db_column='Target_Reps', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Template_Exercises'


class TemplateWorkout(models.Model):
    template_id = models.AutoField(db_column='Template_ID', primary_key=True, blank=True, null=False)
    member = models.ForeignKey('MemberAccount', models.DO_NOTHING, db_column='Member_ID')
    level = models.ForeignKey('Exercise', models.DO_NOTHING, related_name= 'temp_level', db_column='Level')
    category = models.ForeignKey('Exercise', models.DO_NOTHING, related_name='temp_cat', db_column='Category')
    name = models.TextField(db_column='Name')

    class Meta:
        db_table = 'Template_Workout'
