from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    homepage = models.CharField(max_length=100)

class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    content = FroalaField()

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    abstract = FroalaField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()
    content = FroalaField()

    def save(self):
        super(Post, self).save()
        self.slug = slugify(self.title)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tagline(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
