from django.urls import path
from everythingmusic import views

app_name = 'everythingmusic'

urlpatterns = [
    path('', views.album, name='album'),
    path('elelment/', views.element, name='element'),
    path('about-page/', views.about, name='about'),
    path('song-list/<int:album_id>/', views.song_list, name='song_list'),
    path('all-songs/', views.all_songs, name='all_songs'),
    path('listen-now/<int:song_id>/', views.play_song, name='play_song'),
    path('login-page/', views.login_view, name='login_view'),
    path('logout-page/', views.logout_view, name='logout_view'),
    path('contact-page/', views.contact, name='contact'),
    path('register-page/', views.register, name='register'),
    path('add-song/', views.add_song, name='add_song'),
    path('add-artist/', views.add_artist, name='add_artist'),
    path('add-album/', views.add_album, name='add_album'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('edit-profile/<slug:slug>/', views.edit_profile, name='edit_profile'),
    path('delete-song/<slug:slug>/', views.delete_song, name='delete_song'),
    path('artist-song/<int:artist_id>', views.get_song_by_artist, name='get_song_by_artist'),
]
