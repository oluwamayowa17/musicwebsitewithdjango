from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from everythingmusic.models import *
from django.contrib import messages
from everythingmusic.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.

def index(request):
    album = Album.objects.all()
    song = Song.objects.all().order_by('-created')[:15]
    featured_album = Featured.objects.all().order_by('-created')
    featured_song = Featured.objects.all().order_by('-created')
    featured_artist = Featured.objects.all().order_by('-created')
    banner = Banner.objects.all()
    context  = {'album':album, 
                'song':song, 
                'featured_album': featured_album, 
                'featured_artist': featured_artist, 
                'featured_song': featured_song,
                'banner':banner,
                 }
    return render(request, 'frontend/index.html', context)

def album(request):
    album = Album.objects.all().order_by('-created')
    return render(request, 'frontend/albums-store.html', {'album':album})

def song_list(request, album_id):
    get_album = get_object_or_404(Album, id=album_id)
    get_song = Song.objects.filter(album__id=album_id)
    return render(request, 'frontend/song_list.html', {'song':get_song, 'album':get_album})


def about(request):
    about = AboutUs.objects.all()
    return render(request, 'frontend/about.html', {'about':about})

def all_songs(request):
    song = Song.objects.all().order_by('-created')[15:]
    return render(request, 'frontend/song.html', {'song':song})

def play_song(request, song_id):
    get_song = get_object_or_404(Song, id=song_id)
    return render(request, 'frontend/play-song.html', {'song':get_song})

def get_song_by_artist(request, artist_id):
    get_song = Song.objects.filter(artist__id=artist_id)
    return render(request, 'frontend/artist-song.html', {'song': get_song})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = ContactUs(name=name, email=email, phone=phone, message=message)
        subject = 'Everything Music Contacts'
        email_data = {
                'name':name,
                'email':email,
                'phone':phone,
                'message':message
        }
        html_message = render_to_string('frontend/mail-template.html', email_data)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send = mail.send_mail(subject, plain_message, from_email, ['ogungburemayowa2019@gmail.com'], html_message=html_message)
        if send:
            data.save()
            mail.send_mail(subject, plain_message, from_email, [ 'ogungburemayowa2019@gmail.com'], html_message=html_message)
            print(name, email, phone, message)
            messages.success(request, 'Message sent!!') 
        else:
            messages.error(request, 'Could not send email')
    return render(request, 'frontend/contact.html', {})

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('everythingmusic:element')
        else:
            messages.error(request, 'Username or password incorrect!!!')
    return render(request, 'frontend/login.html')

@login_required(login_url='/pages/login-page/')
def logout_view(request):
    logout(request)
    return redirect('everythingmusic:login_view')

@login_required(login_url='/pages/login-page/')
def element(request):
    list_album = Album.objects.count()
    list_song = Song.objects.filter(user=request.user).count()
    return render(request, 'frontend/dashboard.html', {'list':list_album, 'lists':list_song}) 

def register(request):
    if request.method == 'POST':
        reg = RegisterationForm(request.POST)
        if reg.is_valid():
            reg.save()
            messages.success(request, 'User Registered')
            return redirect('everythingmusic:element')
    else:
        reg = RegisterationForm()
    return render(request, 'frontend/register.html', {'reg':reg})

@login_required(login_url='/pages/login-page/')
def add_song(request):
    if request.method == 'POST':
        song = MusicForm(request.POST, request.FILES)
        if song.is_valid():
            var = song.save(commit=False)
            var.user = request.user 
            var.slug = slugify(song.cleaned_data.get('song_name'))
            var.save()
            messages.success(request, 'Song Added')
    else:
        song = MusicForm()
    return render(request, 'frontend/add-song.html', {'song':song})

@login_required(login_url='/pages/login-page/')
def add_artist(request):
    if request.method == 'POST':
        artist = ArtistForm(request.POST, request.FILES)
        if artist.is_valid():
            var = artist.save(commit=False)
            var.user = request.user 
            var.slug = slugify(artist.cleaned_data.get('artist_name'))
            var.save()
            messages.success(request, 'Artist Added')
    else:
        artist = ArtistForm()
    return render(request, 'frontend/add-artist.html', {'artist':artist})

@login_required(login_url='/pages/login-page/')
def add_album(request):
    if request.method == 'POST':
        album = AlbumForm(request.POST, request.FILES)
        if album.is_valid():
            var = album.save(commit=False)
            var.user = request.user 
            var.slug = slugify(album.cleaned_data.get('album_name'))
            var.save()
            messages.success(request, 'Album Added')
    else:
        album = AlbumForm()
    return render(request, 'frontend/add-album.html', {'album':album})

@login_required(login_url='/pages/login-page/')
def view_profile(request):
    list_song = Song.objects.filter(user=request.user)
    return render(request, 'frontend/view-profile.html', {'list':list_song})


@login_required(login_url='/pages/login-page/')
def edit_profile(request, slug):
    get_single_prop = Song.objects.get(slug=slug)
    if request.method == 'POST':
        edit_prop = MusicForm(request.POST, request.FILES, instance=get_single_prop)
        if edit_prop.is_valid():
            edit_prop.save()
            messages.success(request, 'Edit Successful!!!')
    else:
        edit_prop = MusicForm(instance=get_single_prop)
    return render(request, 'frontend/edit-profile.html', {'edit':edit_prop})


@login_required(login_url='/pages/login-page/')
def delete_song(request, slug):
    del_song = Song.objects.get(slug=slug)
    del_song.delete()
    return redirect('everythingmusic:view_profile')

