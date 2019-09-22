from django.conf.urls import url

from product import views

urlpatterns = [
    url(r'^products/$', views.ProductAPIView.as_view(), name='product'),
    url(r'^products/(?P<pk>\d+)/$', views.DeleteProductAPIView.as_view(), name='product1'),
    url(r'addproduct/$', views.AddProductAPIView.as_view(), name='addProduct'),
    url(r'recycle/$',views.ProductsRecycleAPIView.as_view(),name='recycle_bin'),
    url(r'^updateproducts/(?P<pk>\d+)/$', views.UpdateProductAPIView.as_view(), name='updateproduct'),

]
