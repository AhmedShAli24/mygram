from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo


def index(request):
    stored_photos = {}
    all_photos = Photo.objects.all()
    for i in range(len(all_photos)):
        stored_photos[i] = all_photos[i].caption
           
    return render(request, "photos/index.html", {'photos': stored_photos})

def photo_details(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    return HttpResponse("you got the photo %s" % photo.caption)
