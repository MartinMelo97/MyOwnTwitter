"""MyOwnTwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from main import urls as UrlsMain
from tweets import urls as UrlsTweets
from users import urls as UrlsUsers

urlpatterns = [
    url(r'^users/', include(UrlsUsers, namespace="users")),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(UrlsMain, namespace="main")),
    url(r'^tweets/', include(UrlsTweets, namespace="tweets")),
    url(
        regex=r'^media/(?P<path>.*)$',
        view="django.views.static.serve",
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),
]
