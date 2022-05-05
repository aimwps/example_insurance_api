from django.urls import include, path
from .views import LandingPageView, UploadPageView


urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("uploads/", UploadPageView.as_view(), name="upload")


]
