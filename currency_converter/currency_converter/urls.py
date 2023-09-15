from django.contrib import admin
from django.urls import path

from converter.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rates', index)
]