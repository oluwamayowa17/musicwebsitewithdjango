from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    artist_image = models.ImageField(verbose_name = 'Artist Image', null=True, blank=True, upload_to='uploads/', default='uploads/default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.artist_name

    def save(self, *args, **kwargs):
        self.artist_name = self.artist_name.capitalize()
        return super().save(*args, **kwargs)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    album_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    album_image = models.ImageField(verbose_name = 'Album Image', null=True, blank=True, upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.album_name

    def save(self, *args, **kwargs):
        self.album_name = self.album_name.capitalize()
        return super().save(*args, **kwargs)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    song_name = models.CharField(max_length=50)
    image = models.ImageField(verbose_name = 'Song Image', null=True, blank=True, upload_to='uploads/')
    slug = models.SlugField(unique=True)
    audio = models.FileField(null=True, blank=True, upload_to='uploads/')
    lyric = models.TextField(null=True)
    featued_artist = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.song_name

    def save(self, *args, **kwargs):
        self.song_name = self.song_name.capitalize()
        return super().save(*args, **kwargs)

    def get_audio(self):
        if self.audio:
            return self.audio.url   


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class AboutUs(models.Model):
    image = models.ImageField(verbose_name = 'Song Image', null=True, blank=True, upload_to='uploads/')
    content = models.TextField(null=True)



class Banner(models.Model):
    image1 = models.ImageField(verbose_name = 'Banner Image', null=True, blank=True, upload_to='uploads/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)

class Featured(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
