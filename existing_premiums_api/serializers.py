from rest_framework import serializers
from .models import ExistingMedicalPremium

class ExistingMedicalPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingMedicalPremium
        fields = (  "rf_age",
                    "rf_gender",
                    "rf_bmi",
                    "rf_children",
                    "rf_is_smoker",
                    "rf_region",
                    "premium",
                )
