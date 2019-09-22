from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userinfo/(?P<pk>\d+)/$', views.UserinfoAPIView.as_view(), name='userinfo'),
    url(r'^userlist/$', views.UserListAPIView.as_view(), name='userlist'),
    url(r'^deleteuser/(?P<pk>\d+)/$', views.DeleteUserAPIView.as_view(), name='deleteuser'),
    url(r'^adduser/$', views.AddUserAPIView.as_view(), name='adduser'),
]
