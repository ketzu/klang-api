"""vocab_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserViewSet, GroupViewSet
from vocabulary.views import SetViewSet, VocabViewSet, StudiedVocabViewSet

router = routers.DefaultRouter()

#router.register(r'api/v1/users', UserViewSet)
#router.register(r'groups', GroupViewSet)

router.register(r'api/v1/sets', SetViewSet)
router.register(r'api/v1/vocabulary', VocabViewSet)
router.register(r'api/v1/study', StudiedVocabViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api/auth/', include('djoser.urls')),
    url(r'^api/auth/', include('djoser.urls.authtoken')),
    #path('api/auth/web/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api/auth/token/', obtain_auth_token, name='api-token-auth')
]
