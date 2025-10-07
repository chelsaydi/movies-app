"""
URL configuration for video_store1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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




from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', RedirectView.as_view(pattern_name='videos:list', permanent=False)),
    path('', include('videos.urls', namespace='videos')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),               # now /admin/ goes to Django admin
    path('', include('videos.urls', namespace='videos')),
]
