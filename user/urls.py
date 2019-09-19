from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userinfo/(?P<pk>\d+)/$', views.UserinfoAPIView.as_view(), name='userinfo'),
    url(r'^userlist/$', views.UserListAPIView.as_view(), name='userlist')
]
