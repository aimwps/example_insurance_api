from django.urls import include, path
from .views import LandingPageView, UploadPageView, GetDocumentStatusAjax, AddCheckedDocumentAjax


urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("uploads/", UploadPageView.as_view(), name="upload"),
    path("ajax_get_document_status/", GetDocumentStatusAjax, name="ajax-get-documents"),
    path("ajax_add_checked_document/",AddCheckedDocumentAjax, name="add-checked-document"),



]
