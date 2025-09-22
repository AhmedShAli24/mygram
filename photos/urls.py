from django.urls import path

from . import views

app_name = "photos"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:photo_id>", views.details, name="details"),
    path("upload", views.upload_photo, name="upload_photo"),
    path('my_photos', views.my_photos, name='my_photos')
]
