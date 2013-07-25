from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^djmemts/', include('djmemts.urls', namespace='djmemts')),
)
