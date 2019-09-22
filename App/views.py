from django.core.cache import cache
# Create your views here.
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from App.models import Third_app
from App.serializers import Third_appSerializer
from huawei.settings import SECRET_KEY
from tools.mytoken import Token
from user.models import User


class ExampleView(ListModelMixin,
                  GenericAPIView,
                  CreateModelMixin,
                  DestroyModelMixin):
    queryset = Third_app.objects.all()
    serializer_class = Third_appSerializer
    lookup_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({
            'code': 1,
            'msg': '创建成功'
        })

    # 删除
    def delete(self, request, *args, **kwargs):
        # print(self.lookup_field,self.lookup_url_kwarg)
        # print(request.query_params)
        # print(kwargs)
        self.destroy(request, *args, **kwargs)
        return Response({
            'code': 1,
            'msg': '删除成功'
        })


    def get_object(self):
        print(self.lookup_field, self.kwargs)
        print(self.request.query_params)
        if self.lookup_field in self.kwargs:
            return User.objects.get(pk=int(self.kwargs[self.lookup_field]))
        elif 'pk' in self.request.query_params:
            return User.objects.get(pk=int(self.request.query_params['pk']))
        raise Exception("无法获取到正确的请求参数")


class AdminView(CreateAPIView):
    queryset = Third_app.objects.all()
    serializer_class = Third_appSerializer

    def post(self, request, *args, **kwargs):
        action = kwargs.get('action', None)
        if action:
            if action == 'login':
                return self.login(request, *args, **kwargs)
            elif action == 'register':
                return self.register(request, *args, **kwargs)
            return Response({
                'code': -1,
                'msg': '不被支持的请求'
            })
        else:
            raise Exception("action没有值")

    def register(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response({
            'code': 1,
            'msg': '注册成功'
        })

    def login(self, request, *args, **kwargs):
        app_id = request.data.get('username')
        app_secret = request.data.get('password')
        if Third_app.validate_password(app_id, app_secret):
            # 生成token
            token = Token(SECRET_KEY).generate_validate_token(app_id)
            # 把token写入缓存
            cache.set('app_id', token)
            return Response({'code': 1,
                             'msg': '登录成功',
                             'token': token})
        return Response({
            'code': -1,
            'msg': '登录失败'
        })
