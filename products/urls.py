from django.urls.conf import path
from . import views

urlpatterns = [
    path("", views.index),
    path("electronic", views.electronic),
    path("fashion", views.fashion),
    path("jewellery", views.jewellery),
]