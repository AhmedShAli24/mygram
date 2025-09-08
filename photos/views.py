from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo




def index(request):
    stored_photos = []
    all_photos = Photo.objects.all()
    for photo in all_photos:
        stored_photos.append(photo.caption)
    string_photos = "<br>".join(stored_photos)
        
    return HttpResponse(string_photos)

def photo_details(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    return HttpResponse("you got the photo %s" % photo.caption)