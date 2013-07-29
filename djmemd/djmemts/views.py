from django.core.cache import cache
from django.http import HttpResponse, HttpResponseServerError


def test0(request):
    set_value = request.REQUEST.get('v', 1)
    if cache.set('v', set_value):
        get_value = cache.get('v')
        if get_value is not None and get_value != set_value:
            return HttpResponseServerError()
    return HttpResponse()
