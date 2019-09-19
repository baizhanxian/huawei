# Create your views here.

from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.response import Response

from App.serializers import UserinfoSerializer, UserSerializer,UsersSerializer
from App.views import ExampleView
from user.models import User, Userinfo


class UserinfoAPIView(RetrieveDestroyAPIView):
    queryset = Userinfo.objects.all()
    # print(queryset)
    serializer_class = UserinfoSerializer
    # authentication_classes = (MyAuthentication,)
    # permission_classes = (UserListPermission,)



class UserListAPIView(ExampleView):
    queryset = User.objects.all()
    print(queryset)
    serializer_class = UsersSerializer

