# Create your views here.
from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

from App.serializers import \
    ProductsSKUSerializer, \
    AddProductsSKUSerializer, ProductsSerializer
from App.views import ExampleView
from product.models import Products


class ProductAPIView(ExampleView,):
    queryset = Products.objects.filter(is_delete=0)
    serializer_class = ProductsSKUSerializer


class AddProductAPIView(ExampleView):
    queryset = Products.objects.all()
    serializer_class = AddProductsSKUSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = AddProductsSKUSerializer(data=data)
        serializer.is_valid()
        # serializer.save()
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({
            'code': 1,
            'msg': '创建成功'
        })

class DeleteProductAPIView(ExampleView):
    queryset = Products.objects.all()

    serializer_class = ProductsSKUSerializer

    def get_object(self):
        print(self.lookup_field, self.kwargs)
        print(self.request.query_params)
        if self.lookup_field in self.kwargs:
            return Products.objects.get(pk=int(self.kwargs[self.lookup_field]))
        elif 'pk' in self.request.query_params:
            return Products.objects.get(pk=int(self.request.query_params['pk']))
        raise Exception("无法获取到正确的请求参数")


class ProductsRecycleAPIView(ExampleView):
    queryset = Products.objects.filter(is_delete=1)

    serializer_class = ProductsSKUSerializer


class UpdateProductAPIView(UpdateAPIView,UpdateModelMixin):
    queryset = Products.objects.all()

    serializer_class = ProductsSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)