from django.contrib import admin
from everythingmusic.models import *
# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('artist_name', )

    prepopulated_fields = {'slug':('artist_name',)}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('album_name',)}

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=[ 
    'artist', 'album', 'song_name', 'audio', 'created'
]
    prepopulated_fields = {'slug':('song_name',)}

admin.site.register(ContactUs)
admin.site.register(Banner)
admin.site.register(Featured)
admin.site.register(AboutUs)



