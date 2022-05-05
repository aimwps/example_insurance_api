from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("existing_premiums_api.urls")),
    path('', include("baseweb.urls")),
]
