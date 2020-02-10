from django.urls import path
from . import views

urlpatterns = [
    path('', views.decide, name="decide"),
]
