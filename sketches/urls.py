from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'sketches_post_list')
]