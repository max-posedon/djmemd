from django.core.cache import cache
from django.http import HttpResponse


def test0(self):
    cache.get('x')
    return HttpResponse()
