from django.urls import include, path
from rest_framework import routers
from .views import ExistingMedicalPremiumViewSet

router = routers.DefaultRouter()
router.register('medical_premiums',ExistingMedicalPremiumViewSet )
urlpatterns = [
    path("api/", include(router.urls), name='api' ),
    path("medical/", include('rest_framework.urls', namespace="rest_framework"))

]
