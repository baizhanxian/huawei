from rest_framework.serializers import ModelSerializer

from App.models import Third_app
from order.models import Order
from product.models import ProductSKU, Products
from user.models import User, Userinfo


class Third_appSerializer(ModelSerializer):
    class Meta:
        model = Third_app
        fields = ['app_id', 'app_secret']


class UserinfoSerializer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['realname','email','mobile','vip','province','city','country','detail']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserListSerializer(ModelSerializer):
    info = UserinfoSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'info']

class UsersSerializer(ModelSerializer):
    info = UserinfoSerializer()


    class Meta:
        model = User
        fields = ['id','username','info']

    def create(self, validated_data):
        # print(validated_data)
        info_data = validated_data.pop('info')
        # print(info_data[0])

        user = User.objects.create(**validated_data)
        Userinfo.objects.create(user_id=user, **info_data)
        return user


class ProductSKUSerializer(ModelSerializer):
    class Meta:
        model = ProductSKU
        fields = ['name', 'desc', 'price', 'unite', 'inventory', 'sales', 'status']


class ProductsSKUSerializer(ModelSerializer):
    SKU = ProductSKUSerializer(many=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'detail', 'SKU', 'is_delete']



class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'is_delete']


class AddProductsSKUSerializer(ModelSerializer):
    SKU = ProductSKUSerializer()

    class Meta:
        model = Products
        fields = ['id', 'name', 'detail', 'SKU']

    def create(self, validated_data):
        print(validated_data)
        sku_data = validated_data.pop('SKU')
        product = Products.objects.create(**validated_data)
        ProductSKU.objects.create(products=product, **sku_data)
        return product


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_no', 'total_price',
                  'total_count', 'create_time', 'order_status', 'sanp_name',
                  'pay_time', 'confirm_time', 'reply_time','order_notes']


class GetOrderListSerializer(ModelSerializer):
    order = OrderListSerializer(many=True)

    info = UserinfoSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'info', 'order']


class Order_ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'product_id', 'order_id', 'count', 'price']


class OrderProductsSerializer(ModelSerializer):
    product_id = ProductsSKUSerializer()

    class Meta:
        model = Products
        fields = ['id', 'product_id']
