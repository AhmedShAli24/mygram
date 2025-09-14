from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo


def index(request):
    photos = {}
    all_photos = Photo.objects.all()
    print(all_photos)
    for i in range(len(all_photos)):
        photos[all_photos[i].id] = all_photos[i].caption
    print(photos)
           
    return render(request, "photos/index.html", {'photos': photos})

def details(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    return HttpResponse("you got the photo %s" % photo.caption)
