from django.urls import path
from . import views

urlpatterns = [
    path('', views.decide, name="decide"),
    path('download/', views.download, name="download"),
    path('json/', views.json, name="json"),
]
