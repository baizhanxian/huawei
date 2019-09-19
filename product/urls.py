from django.conf.urls import url

from product import views

urlpatterns = [
    url(r'^product/$',views.ProductAPIView.as_view(),name='product')

]
