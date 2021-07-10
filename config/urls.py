"""bookmark_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from datetime import datetime
import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers

from bookmarks.views import BookmarkViewSet


@api_view()
def home(request):
    t = datetime.now()
    return Response({
        'message': 'Bookmark API is up and running.',
        'server_time': t.strftime('%Y-%m-%dT%H:%M:%SZ')
    })


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]

router = routers.SimpleRouter(trailing_slash=False)
router.register('bookmarks', BookmarkViewSet)
urlpatterns += router.urls
