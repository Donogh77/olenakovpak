from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home_post_list'),
]