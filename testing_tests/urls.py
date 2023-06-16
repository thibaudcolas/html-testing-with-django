from django.contrib import admin
from django.urls import path
from django.views.debug import default_urlconf

urlpatterns = [
    path("test/", default_urlconf, name="test_url"),
    path("admin/", admin.site.urls),
]
