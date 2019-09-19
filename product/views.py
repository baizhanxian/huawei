# Create your views here.
from App.serializers import ProductSKUSerializer
from App.views import ExampleView
from product.models import Products


class ProductAPIView(ExampleView):
    queryset = Products.objects.all()
    serializer_class = ProductSKUSerializer
