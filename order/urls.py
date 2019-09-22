from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'getorderlist/$', views.GetOrderListAPIView.as_view(), name='getorderlist'),
    url(r'deleteorderlist/(?P<pk>\d+)/$', views.DeleteOrderListAPIView.as_view(), name='deleteorderlist'),
    url(r'orderproducts/(?P<pk>\d+)/$', views.OrderProductAPIViews.as_view(), name='orderproduncts'),
    url(r'ordersproducts/(?P<pk>\d+)/$', views.OrderProductsAPIViews.as_view(), name='orderproduncts')

]
