# Generated by Django 4.2.1 on 2023-09-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_image_trainer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='workout_schedule',
            field=models.JSONField(blank=True, default={}, null=True),
        ),
    ]
