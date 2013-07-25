from django.conf.urls import patterns, url

urlpatterns = patterns('djmemts.views',
    url(r'0/$', 'test0', name='0'),
)
