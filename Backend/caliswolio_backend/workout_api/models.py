# Hey so I was able to get Django to auto populate some of this but there are things we may want to manually to clean up:
#   * Rearrange models' order
#   * Make sure each ForeignKey and OneToOneField has `on_delete` if it is needed
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Level(models.Model):  #R*
    level_id = models.AutoField(db_column='Level_ID', primary_key=True, blank=True, null=False)
    name = models.TextField(db_column='Name')

    class Meta:
        db_table = 'Level'
    

    class Meta:
        db_table = 'Member_account'

class Exercise(models.Model):  #R*
    exercise_id = models.AutoField(db_column='Exercise_ID', primary_key=True, blank=True, null=False)
    name = models.TextField(db_column='Name')
    category = models.TextField(db_column='Category')
    level_id = models.ForeignKey('Level', models.DO_NOTHING, default= 1, related_name= 'ex_level_id', db_column='Level_ID')
    description = models.TextField(db_column='Description', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'Exercise'


class MemberAccount(models.Model):  #C*R*U*D*
    member_id = models.AutoField(db_column='Member_ID', primary_key=True, blank=True, null=False)
    email = models.TextField(db_column='Email')
    password = models.TextField(db_column='Password')
    phone_number = models.TextField(db_column='Phone_Number')
    level_id = models.ForeignKey('Level', models.DO_NOTHING, default= 1, related_name= 'mem_level_id', db_column='Level_ID')
    birth_year = models.IntegerField(db_column='Birth_Year')
    gender = models.TextField(db_column='Gender')
    zipcode = models.IntegerField(db_column='Zipcode')
    

class FutureWorkout(models.Model):  #CRUD
    future_workout_id = models.AutoField(db_column='Future_Workout_ID', primary_key=True, blank=True, null=False)
    member_id = models.ForeignKey('MemberAccount', models.DO_NOTHING, related_name='future_mem', db_column='Member_ID')
    level_id = models.ForeignKey('Level', models.DO_NOTHING, default= 1, related_name= 'future_level_id', db_column='Level_ID')
    category_id = models.ForeignKey('Exercise', models.DO_NOTHING, related_name='future_cat', db_column='Category')
    name = models.TextField(db_column='Name')
    perform_on = models.DateField(db_column='Perform_On')

    class Meta:
        db_table = 'Future_Workout'


class PriorWorkout(models.Model):  #CRUD
    prior_workout_id = models.AutoField(db_column='Workout_ID', primary_key=True, blank=True, null=False)
    member_id = models.ForeignKey('MemberAccount', models.DO_NOTHING, related_name='pri_mem', db_column='Member_ID')
    level_id = models.ForeignKey('Level', models.DO_NOTHING, default= 1, related_name= 'pri_level_id', db_column='Level_ID')
    category_id = models.ForeignKey('Exercise', models.DO_NOTHING, related_name= 'pri_cat', db_column='Category')
    when_completed = models.DateField(db_column='When_Completed')

    class Meta:
        db_table = 'Prior_Workout'


class TemplateWorkout(models.Model): #CRUD 
    template_id = models.AutoField(db_column='Template_ID', primary_key=True, blank=True, null=False)
    member = models.ForeignKey('MemberAccount', models.DO_NOTHING, related_name='temp_mem', db_column='Member_ID')
    level_id = models.ForeignKey('Level', models.DO_NOTHING, default= 1, related_name= 'temp_level_id', db_column='Level_ID')
    category_id = models.ForeignKey('Exercise', models.DO_NOTHING, related_name='temp_cat', db_column='Category')
    name = models.TextField(db_column='Name')

    class Meta:
        db_table = 'Template_Workout'

class TemplateExercise(models.Model):   #CRUD
    template_ex_id = models.AutoField(db_column='Template_Ex_ID', primary_key=True, blank=True, null=False)
    template_id = models.ForeignKey('TemplateWorkout', models.DO_NOTHING, db_column='Template_ID')
    exercise_id = models.ForeignKey('Exercise', models.DO_NOTHING, db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets', blank=True, null=True)
    target_reps = models.IntegerField(db_column='Target_Reps', blank=True, null=True)
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        db_table = 'Template_Exercise'

class FutureWorkoutExercise(models.Model):   #CRUD
    future_workout_ex_id = models.AutoField(db_column='Future_Workout_Ex_ID', primary_key=True, blank=True, null=False)
    future_workout_id = models.ForeignKey('FutureWorkout', models.DO_NOTHING, db_column='Future_Workout_ID')
    exercise_id = models.ForeignKey('Exercise', models.DO_NOTHING, db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets', blank=True, null=True)
    target_reps = models.IntegerField(db_column='Target_Reps', blank=True, null=True)
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        db_table = 'Future_Workout_Exercise'


class PriorWorkoutExercise(models.Model): #CRUD
    prior_workout_ex_id = models.AutoField(db_column='Prior_Workout_Ex_ID', primary_key=True, blank=True, null=False)
    prior_workout_id = models.ForeignKey('PriorWorkout', models.DO_NOTHING, default= 1, db_column='Prior_Workout_ID')
    exercise_id = models.ForeignKey('Exercise', models.DO_NOTHING, default= 1,  db_column='Exercise_ID')
    target_sets = models.IntegerField(db_column='Target_Sets', blank=True, null=True)
    target_reps = models.IntegerField(db_column='Target_Reps', blank=True, null=True)
    position_in_list = models.IntegerField(db_column='Position_In_List')

    class Meta:
        # managed = False
        db_table = 'Prior_Workout_Exercise'



