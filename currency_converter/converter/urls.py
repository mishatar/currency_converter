from django.urls import path
from .views import Index


urlpatterns = [
    path('rates', Index.as_view(), name="index"),
]