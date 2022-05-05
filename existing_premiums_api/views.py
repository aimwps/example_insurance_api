from rest_framework import viewsets
from .serializers import ExistingMedicalPremiumSerializer
from .models import ExistingMedicalPremium


class ExistingMedicalPremiumViewSet(viewsets.ModelViewSet):
    queryset = ExistingMedicalPremium.objects.all()
    serializer_class = ExistingMedicalPremiumSerializer
