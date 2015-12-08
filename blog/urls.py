from django.conf.urls import url, patterns
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),  # 글 목록
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  # 글 내용

    # post create
    url(r'^new/$', views.post_create, name='post_create'),
    # post update
    url(r'^(?P<pk>\d+)/edit/$', views.post_update, name='post_update'),
    # post delete
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    url(r'^(?P<pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),  # 새 댓글 생성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),  # 새 댓글 수정
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),  # 새 댓글 삭제
]
