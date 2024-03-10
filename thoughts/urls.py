from django.urls import path
from . import views

app_name = 'thoughts'

urlpatterns = [
    path('', views.post_list, name="post_list")
]