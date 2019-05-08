from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'landscape_post_list')
]