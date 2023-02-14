# Generated by Django 4.1.6 on 2023-02-14 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_id', models.AutoField(db_column='Exercise_ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('category', models.TextField(db_column='Category')),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'Exercise',
            },
        ),
        migrations.CreateModel(
            name='FutureWorkout',
            fields=[
                ('future_workout_id', models.AutoField(db_column='Future_Workout_ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('perform_on', models.DateField(db_column='Perform_On')),
                ('category_id', models.ForeignKey(db_column='Category', on_delete=django.db.models.deletion.DO_NOTHING, related_name='future_cat', to='workout_api.exercise')),
            ],
            options={
                'db_table': 'Future_Workout',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.AutoField(db_column='Level_ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
            ],
            options={
                'db_table': 'Member_account',
            },
        ),
        migrations.CreateModel(
            name='MemberAccount',
            fields=[
                ('member_id', models.AutoField(db_column='Member_ID', primary_key=True, serialize=False)),
                ('email', models.TextField(db_column='Email')),
                ('password', models.TextField(db_column='Password')),
                ('phone_number', models.TextField(db_column='Phone_Number')),
                ('birth_year', models.IntegerField(db_column='Birth_Year')),
                ('gender', models.TextField(db_column='Gender')),
                ('zipcode', models.IntegerField(db_column='Zipcode')),
                ('level_id', models.ForeignKey(db_column='Level_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mem_level_id', to='workout_api.level')),
            ],
        ),
        migrations.CreateModel(
            name='PriorWorkout',
            fields=[
                ('prior_workout_id', models.AutoField(db_column='Workout_ID', primary_key=True, serialize=False)),
                ('when_completed', models.DateField(db_column='When_Completed')),
                ('category_id', models.ForeignKey(db_column='Category', on_delete=django.db.models.deletion.DO_NOTHING, related_name='pri_cat', to='workout_api.exercise')),
                ('level_id', models.ForeignKey(db_column='Level_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pri_level_id', to='workout_api.level')),
                ('member_id', models.ForeignKey(db_column='Member_ID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='pri_mem', to='workout_api.memberaccount')),
            ],
            options={
                'db_table': 'Prior_Workout',
            },
        ),
        migrations.CreateModel(
            name='TemplateWorkout',
            fields=[
                ('template_id', models.AutoField(db_column='Template_ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('category_id', models.ForeignKey(db_column='Category', on_delete=django.db.models.deletion.DO_NOTHING, related_name='temp_cat', to='workout_api.exercise')),
                ('level_id', models.ForeignKey(db_column='Level_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='temp_level_id', to='workout_api.level')),
                ('member', models.ForeignKey(db_column='Member_ID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='temp_mem', to='workout_api.memberaccount')),
            ],
            options={
                'db_table': 'Template_Workout',
            },
        ),
        migrations.CreateModel(
            name='TemplateExercise',
            fields=[
                ('template_ex_id', models.AutoField(db_column='Template_Ex_ID', primary_key=True, serialize=False)),
                ('target_sets', models.IntegerField(blank=True, db_column='Target_Sets', null=True)),
                ('target_reps', models.IntegerField(blank=True, db_column='Target_Reps', null=True)),
                ('position_in_list', models.IntegerField(db_column='Position_In_List')),
                ('exercise_id', models.ForeignKey(db_column='Exercise_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='workout_api.exercise')),
                ('template_id', models.ForeignKey(db_column='Template_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='workout_api.templateworkout')),
            ],
            options={
                'db_table': 'Template_Exercise',
            },
        ),
        migrations.CreateModel(
            name='PriorWorkoutExercise',
            fields=[
                ('prior_workout_ex_id', models.AutoField(db_column='Prior_Workout_Ex_ID', primary_key=True, serialize=False)),
                ('target_sets', models.IntegerField(blank=True, db_column='Target_Sets', null=True)),
                ('target_reps', models.IntegerField(blank=True, db_column='Target_Reps', null=True)),
                ('position_in_list', models.IntegerField(db_column='Position_In_List')),
                ('exercise_id', models.ForeignKey(db_column='Exercise_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='workout_api.exercise')),
                ('prior_workout_id', models.ForeignKey(db_column='Prior_Workout_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='workout_api.priorworkout')),
            ],
            options={
                'db_table': 'Prior_Workout_Exercise',
            },
        ),
        migrations.CreateModel(
            name='FutureWorkoutExercise',
            fields=[
                ('future_workout_ex_id', models.AutoField(db_column='Future_Workout_Ex_ID', primary_key=True, serialize=False)),
                ('target_sets', models.IntegerField(blank=True, db_column='Target_Sets', null=True)),
                ('target_reps', models.IntegerField(blank=True, db_column='Target_Reps', null=True)),
                ('position_in_list', models.IntegerField(db_column='Position_In_List')),
                ('exercise_id', models.ForeignKey(db_column='Exercise_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='workout_api.exercise')),
                ('future_workout_id', models.ForeignKey(db_column='Future_Workout_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='workout_api.futureworkout')),
            ],
            options={
                'db_table': 'Future_Workout_Exercise',
            },
        ),
        migrations.AddField(
            model_name='futureworkout',
            name='level_id',
            field=models.ForeignKey(db_column='Level_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='future_level_id', to='workout_api.level'),
        ),
        migrations.AddField(
            model_name='futureworkout',
            name='member_id',
            field=models.ForeignKey(db_column='Member_ID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='future_mem', to='workout_api.memberaccount'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='level_id',
            field=models.ForeignKey(db_column='Level_ID', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ex_level_id', to='workout_api.level'),
        ),
    ]
