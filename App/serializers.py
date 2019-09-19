from rest_framework.serializers import ModelSerializer

from App.models import Third_app
from product.models import Products, ProductSKU
from user.models import User, Userinfo


class Third_appSerializer(ModelSerializer):
    class Meta:
        model = Third_app
        fields = ['app_id', 'app_secret', 'app_description ']


class UserinfoSerializer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['realname','email','mobile','vip','province','city','country','detail']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UsersSerializer(ModelSerializer):
    info = UserinfoSerializer(read_only=True,many=True)

    class Meta:
        model = User
        fields = ['id','username','info']


class ProductSKUSerializer(ModelSerializer):
    class Meta:
        model = ProductSKU
        fields = ['name', 'desc','price','unite','inventory','sales','status','']
