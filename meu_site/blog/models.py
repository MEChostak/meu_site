from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, 
                                choices=STATUS,
                                default='rascunho')
    

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title



# Create your models here.
