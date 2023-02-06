# Hey so I was able to get Django to auto populate some of this but there are things we may want to manually to clean up:
#   * Rearrange models' order
#   * Make sure each ForeignKey and OneToOneField has `on_delete` if it is needed
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Exercise(models.Model):
    exercise_id = models.AutoField(db_column='Exercise_ID', primary_key=True, blank=True, null=True)
    ex_name = models.TextField(db_column='Ex_Name')
    description = models.TextField(db_column='Description')

    class Meta:
        managed = False
        db_table = 'Exercise'


class ExerciseCategory(models.Model):
    ex_cat_id = models.AutoField(db_column='Ex_Cat_ID', primary_key=True, blank=True, null=True)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='Exercise_ID')
    cat = models.ForeignKey('WorkoutCategory', models.DO_NOTHING, db_column='Cat_ID')
    num_of_exercises = models.TextField(db_column='Num_Of_Exercises')

    class Meta:
        managed = False
        db_table = 'Exercise_Category'


class ExerciseLevel(models.Model):
    ex_level_id = models.AutoField(db_column='Ex_Level_ID', primary_key=True, blank=True, null=True)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='Exercise_ID')
    level = models.ForeignKey('WorkoutLevel', models.DO_NOTHING, db_column='Level_ID')
    default_target_sets = models.IntegerField(db_column='Default_Target_Sets')
    default_target_reps = models.IntegerField(db_column='Default_Target_Reps')

    class Meta:
        managed = False
        db_table = 'Exercise_Level'


class FutureWorkout(models.Model):
    future_workout_id = models.AutoField(db_column='Future_Workout_ID', primary_key=True, blank=True, null=True)
    member = models.ForeignKey('Member_account', models.DO_NOTHING, db_column='Member_ID')
    level = models.ForeignKey('WorkoutLevel', models.DO_NOTHING, db_column='Level_ID')
    category = models.ForeignKey('WorkoutCategory', models.DO_NOTHING, db_column='Cat_ID')
    name = models.TextField(db_column='Name')
    perform_on = models.DateField(db_column='Perform_On')

    class Meta:
        db_table = 'Future_Workout'


class FutureWorkoutExercises(models.Model):
    future_workout_ex_id = models.AutoField(db_column='Future_Workout_Ex_ID', primary_key=True, blank=True, null=True)
    future_workout = models.ForeignKey('FutureWorkout', models.DO_NOTHING, db_column='Future_Workout_ID')
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets')
    target_reps = models.IntegerField(db_column='Target_Reps')
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        db_table = 'Future_Workout_Exercises'


class MemberAccount(models.Model):
    member_id = models.AutoField(db_column='Member_ID', primary_key=True, blank=True, null=True)
    email = models.TextField(db_column='Email')
    password = models.TextField(db_column='Password') 
    phone_number = models.TextField(db_column='Phone_Number') 
    level_id = models.IntegerField(db_column='Level_ID')  
    birth_year = models.IntegerField(db_column='Birth_Year')   
    gender = models.TextField(db_column='Gender')  
    zipcode = models.IntegerField(db_column='Zipcode')  

    class Meta:
        db_table = 'Member_account'


class PriorWorkout(models.Model):
    # Needs Completion
    #########################

    class Meta:
        db_table = 'Prior_Workout'


class PriorWorkoutExercises(models.Model):
    prior_workout_ex_id = models.AutoField(db_column='Prior_Workout_Ex_ID', primary_key=True, blank=True, null=True)
    exercise_id = models.IntegerField(db_column='Exercise_ID')
    workout = models.ForeignKey('PriorWorkout', models.DO_NOTHING, db_column='Workout_ID')
    target_sets = models.IntegerField(db_column='Target_Sets')
    target_reps = models.IntegerField(db_column='Target_Reps')
    actual_sets = models.IntegerField(db_column='Actual_Sets')
    actual_reps = models.IntegerField(db_column='Actual_Reps')
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        db_table = 'Prior_Workout_Exercises'


class TemplateExercises(models.Model):
    template_ex_id = models.AutoField(db_column='Template_Ex_ID', primary_key=True, blank=True, null=True)
    template = models.ForeignKey('TemplateWorkout', models.DO_NOTHING, db_column='Template_ID')
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets')
    target_reps = models.IntegerField(db_column='Target_Reps')

    class Meta:
        managed = False  # May need change
        db_table = 'Template_Exercises'


class TemplateWorkout(models.Model):
    # Needs Completion
    ###########################
    class Meta:
        db_table = 'Template_Workout'


class WorkoutCategory(models.Model):
    cat_id = models.AutoField(db_column='Cat_ID', primary_key=True, blank=True, null=True)
    description = models.TextField(db_column='Description')
    name = models.TextField(db_column='Name')

    class Meta:
        managed = False
        db_table = 'Workout_Category'


class WorkoutLevel(models.Model):
    level_id = models.AutoField(db_column='Level_ID', primary_key=True, blank=True, null=True)
    description = models.TextField(db_column='Description')
    name = models.TextField(db_column='Name')

    class Meta:
        managed = False
        db_table = 'Workout_Level'
