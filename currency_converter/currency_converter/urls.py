from django.contrib import admin
from django.urls import path, re_path

from converter.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rates', index)
]
# (?:page-(?P<page_number>\d+)/)?$