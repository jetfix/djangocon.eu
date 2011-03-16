from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


handler500 = 'utils.views.server_error'

urlpatterns = patterns('',
    (r'^', include('core.urls', namespace='core', app_name='core')),
    (r'^', include('subscribers.urls')),
    (r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    (r'^accommodation/', include('accommodation.urls', namespace='accommodation', app_name='accommodation')),
    (r'^talks/', include('talks.urls', namespace='talks', app_name='talks')),
    (r'^barn/', include(admin.site.urls)),
)

urlpatterns += patterns('utils.views',
    url(r'^flush_cache/$', 'flush_cache', name='flush_cache'),
)
