from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.CharField(max_length=250, default="Anonymous") # author name
    publish = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    class Meta:
        ordering = ('-publish',)

    def __str__(self) -> str:
        return self.title
