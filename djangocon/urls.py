from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

handler500 = 'djangocon.utils.views.server_error'

urlpatterns = patterns('',
    (r'^barn/', include(admin.site.urls)),
)

urlpatterns += patterns('djangocon',
    url(r'^$', 'subscribers.views.home', name='home'),
    url(r'^clear/$', 'subscribers.views.clear', name='clear'),
    url(r'^talks/', include('djangocon.talks.urls'), name='talks'),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^legal/$', 'direct_to_template', {'template': 'legal_notices.html'}, name='legal_notices'),
    url(r'^register/$', 'direct_to_template', {'template': 'register.html'}, name='register'),
)

# Static Media File Serving
if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )
