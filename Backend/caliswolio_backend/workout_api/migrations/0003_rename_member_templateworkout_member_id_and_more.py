# Generated by Django 4.0.3 on 2023-03-12 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_api', '0002_remove_futureworkout_category_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templateworkout',
            old_name='member',
            new_name='member_id',
        ),
        migrations.AlterModelTable(
            name='level',
            table='Level',
        ),
        migrations.AlterModelTable(
            name='memberaccount',
            table='Member_account',
        ),
    ]
