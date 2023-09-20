from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    national_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    name =  models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Trainee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add fields specific to trainees
    fitness_goal = models.CharField(max_length=100)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    bmi = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    workout_schedule = models.JSONField(default={},  null=True, blank=True)
    trainer = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.email
    
    def calculate_bmi(self):
        if self.height and self.weight:
            height_in_meters = self.height / 100.0  # Convert height to meters
            bmi_value = self.weight / (height_in_meters ** 2)  # Calculate BMI
            return round(bmi_value, 2)
        else:
            return None

    def save(self, *args, **kwargs):
        self.bmi = self.calculate_bmi()  # Calculate BMI
        super().save(*args, **kwargs)



class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add fields specific to trainers
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='trainer_images/', null=True, blank=True)


    def __str__(self):
        return self.user.email

from django.db import models

class Tutorial(models.Model):
    MUSCLE_GROUP_CHOICES = [
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Legs', 'Legs'),
        ('Arms', 'Arms'),
        ('Shoulders', 'Shoulders'),
        ('Core', 'Core'),
        ('Other', 'Other'),
    ]
    MUSCLE_NAME_CHOICES = [
        ('PecMayori', 'Pec Mayori'),
        ('Oblique', 'Oblique'),
        ('Neck', 'Neck'),
        ('Deltoids_Front', 'Deltoids Front'),
        ('GROINS', 'GROINS'),
        ('QUADS', 'QUADS'),
        ('knee', 'knee'),
        ('Brachii_short_Head', 'Brachii short Head'),
        ('Tibialis_Anterior', 'Tibialis Anterior'),
        ('shin', 'shin'),
        ('Brachioradialis', 'Brachioradialis'),
        ('Abdominis', 'Abdominis'),
        ('Digitorum', 'Digitorum'),
        ('Brachii_Long_Head', 'Brachii Long Head'),
        ('CALVES', 'CALVES'),
        ('PERONEALS', 'PERONEALS'),
        ('Trapezius', 'Trapezius'),
        ('Deltoids_Back', 'Deltoids Back'),
        ('Latissimus_Dorsi', 'Latissimus Dorsi'),
        ('TricepsMedial', 'Triceps Medial'),
        ('ErectorSpinae', 'Erector Spinae'),
        ('ExtensorDigitorum', 'Extensor Digitorum'),
        ('FlexorCarpi', 'Flexor Carpi'),
        ('GLUTES', 'GLUTES'),
        ('TricepsLateral', 'Triceps Lateral'),
    ]

    name = models.CharField(max_length=100)
    muscle_name = models.CharField(max_length=100, choices=MUSCLE_NAME_CHOICES)
    muscle_group = models.CharField(max_length=10, choices=MUSCLE_GROUP_CHOICES)
    grade = models.PositiveIntegerField()
    video = models.FileField(upload_to='tutorial_videos/', null=True, blank=True)

    def __str__(self):
        return self.name


