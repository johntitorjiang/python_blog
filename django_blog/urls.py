"""django_blog URL Configuration

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
from django.conf.urls import url, include
from django.views.static import serve

import xadmin

from django_blog.settings import MEDIA_ROOT
from article import views
from article.views import DetailView, HomepageView, ArchivesView, AboutmeView, TagView, SearchView
# from django.contrib import admin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^archives/$', ArchivesView.as_view(), name='archives'),
    url(r'^about_me/$', AboutmeView.as_view(), name='about_me'),
    url(r'^(?P<tag>\w+)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

]

# 全局404
handler404 = 'article.views.page_not_found'