# Create your views here.

from App.serializers import GetOrderListSerializer, OrderProductsSerializer
from App.views import ExampleView
from order.models import order_product, Order
from user.models import User

pk = None


class GetOrderListAPIView(ExampleView):
    queryset = User.objects.all()

    serializer_class = GetOrderListSerializer


class DeleteOrderListAPIView(ExampleView):
    queryset = User.objects.all()

    serializer_class = GetOrderListSerializer

    def get_object(self):
        print(self.lookup_field, self.kwargs)
        print(self.request.query_params)
        if self.lookup_field in self.kwargs:
            return Order.objects.get(pk=int(self.kwargs[self.lookup_field]))
        elif 'pk' in self.request.query_params:
            return Order.objects.get(pk=int(self.request.query_params['pk']))
        raise Exception("无法获取到正确的请求参数")


class OrderProductAPIViews(ExampleView):
    global pk

    queryset = order_product.objects.filter(order_id=2)
    serializer_class = OrderProductsSerializer
    lookup_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        print(request, kwargs)
        global pk
        pk = kwargs['pk']

        return self.list(request, *args, **kwargs)


class OrderProductsAPIViews(ExampleView):
    global pk

    queryset = order_product.objects.filter(order_id=1)
    serializer_class = OrderProductsSerializer
