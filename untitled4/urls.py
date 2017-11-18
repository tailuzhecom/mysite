"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog.views import get_detail, login, blog_list, main_site

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detail/(\d+)/$', get_detail, name='blog_get_detail'),
    url(r'^login/', login, name='blog_login'),
    url(r'^blog_list/', blog_list, name='blog_list'),
    url(r'^main_site/', main_site, name='main_site')
]
