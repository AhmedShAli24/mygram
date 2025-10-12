from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm


def index(request):
    photos = {}
    all_photos = Photo.objects.all()
    print(all_photos)
    for i in range(len(all_photos)):
        photos[all_photos[i].id] = all_photos[i].caption
    print(photos)
           
    return render(request, "photos/index.html", {'photos': photos})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photos:my_photos')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_photo.html', {'form': form})   

@login_required
def my_photos(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'photos/my_photos.html', {'photos': photos})
        
        
def details(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    return HttpResponse("you got the photo %s" % photo.caption)

def search(request):
    User = get_user_model()
    searched = request.GET.get('searched', '')
    if searched:
        """
        select u.*
        from users u
        where u.username ilike '%ahmed%'
        limit 1;
        """
        searched_user = User.objects.filter(username__icontains = searched)
        """
        select p.*
        from photos p
        left join users u on (u.id = p.user_id)
        where u.username ilike '%ahmed%';
        """
        photos = Photo.objects.filter(user__username__icontains=searched)
        
        print("=====================")
        print(searched_user.query)
        print("=====================")
        print(photos.query)
        print("=====================")
        
    return render(request, 'photos/searched.html',  {'searched_user': searched_user.first(), 'photos': photos} )
        
