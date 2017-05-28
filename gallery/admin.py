from django.contrib import admin

from django.contrib import admin
from .models import Album
from .models import Artwork

admin.site.register(Album)
admin.site.register(Artwork)
