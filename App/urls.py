from django.conf.urls import url

from App import views

urlpatterns = [


    url(r'^admin/(?P<action>\w+)/$', views.AdminView.as_view(), name='admin'),

]
