from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),
)


