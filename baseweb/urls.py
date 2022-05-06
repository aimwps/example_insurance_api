from django.urls import include, path
from .views import LandingPageView, UploadPageView, GetDocumentStatusAjax


urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("uploads/", UploadPageView.as_view(), name="upload"),
    path("ajax_get_document_status/", GetDocumentStatusAjax, name="ajax-get-documents"),


]
