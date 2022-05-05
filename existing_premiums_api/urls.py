from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path("api/", include(router.urls)),
    path("existing-premiums-api/", include('rest_framework.urls', namespace="rest_framework"))

]
