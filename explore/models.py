from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("explore:webpage_list_by_category", args=[self.slug])
    
    
class WebPage(models.Model):
    category = models.ManyToManyField(Category, related_name='webpages', blank=True)

    name = models.CharField(max_length=100, db_index=True)
    link = models.CharField(max_length=500, db_index=True)
    description = models.CharField(max_length=200)
    
    likes = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_description(self):
        return self.description
