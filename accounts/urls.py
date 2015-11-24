from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
]
