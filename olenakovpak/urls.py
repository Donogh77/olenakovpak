"""olenakovpak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('works/', include('works.urls')),
    path('eventsandworkshops/', include('eventsandworkshops.urls')),
    path('blog/', include('blog.urls')),
    path('contacts/', views.contacts, name='contacts'),
    path('works/botanical/', include('botanical.urls')),
    path('works/genre/', include('genre.urls')),
    path('works/illustrations/', include('illustrations.urls')),
    path('works/still/', include('still.urls')),
    path('works/landscape/', include('landscape.urls')),
    path('works/sketches/', include('sketches.urls')),
    path('static/', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)