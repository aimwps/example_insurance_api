
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ExistingMedicalPremium(models.Model):
    gender_choices = (("female", "Female"),("male", "Male"),)
    region_choices = (("northwest", "North West"), ("northeast", "North East"), ("southeast", "South East"), ("southwest", "South West"))
    rf_age = models.PositiveIntegerField()
    rf_gender = models.CharField(max_length=255, choices=gender_choices)
    rf_bmi = models.DecimalField(max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), ], )
    rf_children = models.PositiveIntegerField()
    rf_is_smoker = models.BooleanField()
    rf_region = models.CharField(max_length=255, choices=region_choices)
    premium = models.DecimalField(max_digits=13, decimal_places=2)
