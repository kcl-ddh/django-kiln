from django.conf.urls import patterns, url

urlpatterns = patterns('kiln.views',
                       url(r'^(?P<kiln_url>[^?]*)$', 'process',
                           {'template': 'process.html'}, name='kiln'),
                       )
