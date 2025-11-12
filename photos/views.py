from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.urls import reverse
from .models import Photo, UserPhotoLikes, UserComments
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
    print(User)
    searched = request.GET.get('searched', '')
    print(searched)
    
    searched_user = User.objects.filter(username__icontains = searched).first()
    photos = Photo.objects.filter(user__username__icontains=searched)
    
    if request.method == 'POST':
        photo_id = request.POST.get('photo_id')
        print(photo_id)
        user_id = request.user.id
        print("+++++++++++++++++")
        print(user_id)
        
        ## if it doesn't exist in UserPhotoLike create it
        userliked = UserPhotoLikes.objects.filter(user = user_id, photo = photo_id).first()
        print(userliked)
        if userliked:
            userliked.delete()
        else:
            new_user_like = UserPhotoLikes(user_id = user_id, photo_id = photo_id)
            new_user_like.save()
            print(new_user_like)
        
        # photo = get_object_or_404(Photo, id=photo_id)
        # print(photo)
        # if photo.likes == 0:
        #     photo.likes += 1
        # else:
        #     photo.likes+=0
        # photo.save()
        
        search_url = reverse('photos:search')
        print("################")
        print(search_url)
        return redirect(f"{search_url}?searched={searched}")
    
    #   
    user_list_of_photo = UserPhotoLikes.objects.filter(user = request.user)
    list_of_user_likes = set()
    for userPhoto in user_list_of_photo:
        print(userPhoto.photo.id)
        list_of_user_likes.add(userPhoto.photo.id)
        
   
    return render(request, 'photos/searched.html',  {
        'searched_user': searched_user,
        'photos': photos,
        'searched': searched,
        'list_of_user_likes': list_of_user_likes
    })


def comments(request, photo_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        search = request.POST.get('searched')
        
        photo = Photo.objects.get(id = photo_id)
        
        if comment_text:
            UserComments.objects.create(user = request.user, photo = photo, comment = comment_text)
        return redirect(f"{reverse('photos:search')}?searched={search}")
        
