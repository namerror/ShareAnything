from django.urls import path
from . import views

app_name = 'explore'

urlpatterns = [
    path('', views.list, name='webpage_list'),
    path('<slug:category_slug>/', views.list, name='webpage_list_by_category'),
]