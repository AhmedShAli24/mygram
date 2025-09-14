from django.urls import path

from . import views

app_name = "photos"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:photo_id>", views.details, name="details"),
]