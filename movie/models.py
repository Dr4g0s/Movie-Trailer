from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from multiselectfield import MultiSelectField
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


CATEGORY_CHOICES = (
    ('Action' , 'Action'),
    ('Adventure','Adventure'),
    ('Comedy' , 'Comedy'),
    ('Drama'  , 'Drama'),
    ('Romance', 'Romance'),
)

LANGUAGES_CHOICES = (
    ('EN', 'English'),
    ('GE', 'German'),
)


class Movie(models.Model):
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(max_length=100, blank=True, unique=True)
    trailer     = models.URLField()
    image       = models.ImageField(upload_to="movies/")
    banner      = models.ImageField(upload_to="movies/banners/")
    description = models.TextField(blank=True)
    cast        = TaggableManager()
    category    = MultiSelectField(choices=CATEGORY_CHOICES, max_length=25, max_choices=4)
    language    = models.CharField(choices=LANGUAGES_CHOICES, max_length=2)
    year        = models.DateField()
    views       = models.IntegerField(default=0)
    created     = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])


LINKS_TYPE = (
    ('D', 'Download'),
    ('W', 'Watch'),
)

class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_links', on_delete=models.CASCADE)
    type  = models.CharField(choices=LINKS_TYPE, max_length=1)
    link  = models.URLField()

    def __str__(self):
        return '{} link for {}'.format(self.type, self.movie)

class Contact(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
