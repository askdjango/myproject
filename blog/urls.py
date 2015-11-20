from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),  # 글 목록
    url(r'^detail/(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),  # 글 내용
    url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views.comment_new', name='comment_new'),  # 새 댓글 생성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit', name='comment_edit'),  # 새 댓글 수정
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'blog.views.comment_delete', name='comment_delete'),  # 새 댓글 삭제
    url(r'^new/$', 'blog.views.post_new', name='post_new'),  # 새 포스팅 등록
]
