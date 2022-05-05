
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

## Client Instructions for modelling data
# Create a database to retain data for existing medical inusurance premiums
    # Add risk factors(RF) that are used to calculate the premium.
        # The age of the proposer as an integer
        # The gender of the proposer, male or female
        # The BMI of the proposer, a rational number to 1 decimal place
        # The number of children the proposer has as an integer
        # The smoker status of the proposer, true or false
        # The region where the proposer, described as a point of a compass
    # The premium for the policy - a rational number to 2 decial places

class ExistingMedicalPremium(models.Model):
    gender_choices = (("female", "Female"),("male", "Male"),)
    region_choices = (("northwest", "North West"), ("northeast", "North East"), ("southeast", "South East"), ("southwest", "South West"))
    rf_age = models.PositiveIntegerField()
    rf_gender = models.CharField(max_length=255, choices=gender_choices)
    rf_bmi = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), ], )
    rf_children = models.PositiveIntegerField()
    rf_is_smoker = models.BooleanField()
    rf_region = models.CharField(max_length=255, choices=region_choices)
    premium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00), ], )
