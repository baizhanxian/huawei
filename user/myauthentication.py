from django.core.cache import cache
from rest_framework.authentication import BasicAuthentication

from user.models import User
from huawei.settings import SECRET_KEY
from tools.mytoken import Token

#自定义的认证类
class MyAuthentication(BasicAuthentication):
    def authenticate(self, request):
        clent_token = request.query_params.get('token', None)
        cache_token = cache.get('username')
        # print(cache_token,clent_token)
        if clent_token == cache_token:
            try:
                res = Token(SECRET_KEY).confirm_validate_token(clent_token)
                user = User.objects.get(username=res)
                #成功，返回二元组
                return user,clent_token
            except Exception as e:
                print(e)

