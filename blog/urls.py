from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog_post_list'),
    #path('media/<path>.*', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]