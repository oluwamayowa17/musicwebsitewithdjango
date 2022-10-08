from django import forms
from everythingmusic.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators

class RegisterationForm(UserCreationForm):
    username = forms.CharField(
        label='Username*',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label='Password*',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password*',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    first_name = forms.CharField(
        required=False,
        label='Firstname',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    last_name = forms.CharField(
        required=False,
        label='Lastname',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user


class MusicForm(forms.ModelForm):
    song_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'},
    ))
   
    artist = forms.ModelChoiceField(
        empty_label='Select Artist',
        queryset=Artist.objects.all(),
        widget=forms.Select(
        attrs={'class':'form-control'},
        ))

    album = forms.ModelChoiceField(
        empty_label='Select Album',
        queryset=Album.objects.all(),
        required=False,
        widget=forms.Select(
        attrs={'class':'form-control'}))

    image = forms.ImageField(
        required=False
    )

    audio = forms.FileField()


    botcatcher = forms.CharField(
        required=False, 
        widget=forms.HiddenInput, 
        validators=[validators.MaxLengthValidator(0)])

    lyric = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class':'form-control'}
        )
    )

    featued_artist = forms.CharField(
        label='Featured Artist(if any)',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )


    class Meta():
        model = Song
        exclude = ['created', 'modified', 'user', 'slug', 'popular']


class ArtistForm(forms.ModelForm):
    artist_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'},
    ))


    popular = forms.BooleanField(
        required=False,
        initial = False,
    )

    class Meta():
        model = Artist
        exclude = ['created', 'modified', 'user', 'slug']

    def clean_artist_name(self):
        name = self.cleaned_data.get('artist_name')
        if Artist.objects.filter(artist_name=name).exists():
            raise forms.ValidationError('Artist Already Exist')
        return name



class AlbumForm(forms.ModelForm):
    album_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'},
    ))

    artist = forms.ModelChoiceField(
        empty_label='Select Artist',
        queryset=Artist.objects.all(),
        widget=forms.Select(
        attrs={'class':'form-control'},
        ))
        
    album_image = forms.ImageField()

    popular = forms.BooleanField(
        required=False,
        initial = False,
    )

    class Meta():
        model = Album
        exclude = ['created', 'modified', 'user', 'slug']

    def clean_album_name(self):
        name = self.cleaned_data.get('album_name')
        if Album.objects.filter(album_name=name).exists():
            raise forms.ValidationError('Album Already Exist')
        return name    

