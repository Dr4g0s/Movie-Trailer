from django.contrib import admin
from .models import Movie, MovieLinks, Contact
# Register your models here.

admin.site.register(MovieLinks)

admin.site.register(Contact)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display  = ['title', 'slug', 'category', 'language', 'year', 'views', 'created']
    list_filter   = ['language', 'year', 'views', 'created']
    search_fields = ['title',]
