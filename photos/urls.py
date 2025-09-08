from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:photo_id>", views.photo_details, name="photo_details")
]