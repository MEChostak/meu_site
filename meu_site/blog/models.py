from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls.base import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='publish')

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, 
                                choices=STATUS,
                                default='rascunho')
    
 
    object = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse("post_detail", args= [self.pk])

    def get_absolute_url_update(self):
        return reverse("post_edit", args= [self.pk])
    
    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title



# Create your models here.
