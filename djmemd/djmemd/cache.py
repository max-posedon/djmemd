from django.core.cache.backends.memcached import MemcachedCache, PyLibMCCache
from django_pylibmc.memcached import PyLibMCCache as DjangoPyLibMCCache


class MemcachedCache2(MemcachedCache):
    def close(self, **kwargs):
        pass

class PyLibMCCache2(PyLibMCCache):
    def close(self, **kwargs):
        pass

class DjangoPyLibMCCache2(DjangoPyLibMCCache):
    def close(self, **kwargs):
        pass
