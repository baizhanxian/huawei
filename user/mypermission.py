from rest_framework.permissions import BasePermission

from user.models import User


class UserListPermission(BasePermission):
    def has_permission(self, request, view):
        #如果登录，则有权限
        if isinstance(request.user,User):
            return True
        return False
    #对象级别的权限
    def has_object_permission(self, request, view, obj):
        print(obj,'1111')
        if request.method in ['POST','PUT','DELETE']:
            if request.user and request.user.type == 1:
                return True
        #get请求，并且返回的obj是当前用户则有权限
        elif request.method == 'GET' and request.user == obj:
            return True
        return False