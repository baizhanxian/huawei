# Create your views here.
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.response import Response

from App.serializers import UserinfoSerializer, UsersSerializer, UserListSerializer
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

    serializer_class = UserListSerializer



class DeleteUserAPIView(ExampleView):
    queryset = User.objects.all()

    serializer_class = UsersSerializer


class AddUserAPIView(ExampleView):
    queryset = User.objects.all()

    serializer_class = UsersSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = UsersSerializer(data=data)
        serializer.is_valid()
        # serializer.save()
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({
            'code': 1,
            'msg': '创建成功'
        })
