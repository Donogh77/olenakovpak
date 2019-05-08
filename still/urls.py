from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'still_post_list')
]