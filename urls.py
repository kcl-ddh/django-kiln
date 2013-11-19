from django.conf.urls import patterns, url

urlpatterns = patterns('kiln.views',
                       url(r'^(?P<parameters>[^?]*)/$', 'process',
                           {'template': 'process.html'}, name='kiln'),
                       )
