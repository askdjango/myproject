"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),  # 글 목록
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail'),  # 글 내용
    url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views.comment_new'),  # 새 댓글 생성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit'),  # 새 댓글 수정

    url(r'^new/$', 'blog.views.post_new'),  # 새 포스팅 등록
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)