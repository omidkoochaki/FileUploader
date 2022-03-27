from django.urls import path
from .views import schema_view

urlpatterns = [
    path('docs/', schema_view, name="upload"),
    ]
