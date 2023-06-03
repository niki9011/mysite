from django.urls import path
from .views import certifications

urlpatterns = [
    path('certifications/', certifications, name="certifications"),
]
