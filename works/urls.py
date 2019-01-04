from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='works_post_list'),
]