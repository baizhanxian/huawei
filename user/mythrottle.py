from rest_framework.throttling import SimpleRateThrottle


class MyThrottle(SimpleRateThrottle):
    rate = '5/m'
    def get_cache_key(self, request, view):
        return self.get_ident(request)