from django.urls import path
from . import views

urlpatterns = [
    path('EditPage/<str:pk>', views.edit, name="Edit")
]
