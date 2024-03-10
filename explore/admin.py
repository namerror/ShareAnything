from django.contrib import admin
from .models import WebPage, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
class WebPageAdmin(admin.ModelAdmin):
    fields = ["name", "link", "description", "likes", "category"]

# Register your models here.
admin.site.register(WebPage, WebPageAdmin)
admin.site.register(Category, CategoryAdmin)