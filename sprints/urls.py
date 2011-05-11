from django.conf.urls.defaults import *

from django.views.generic.simple import redirect_to

urlpatterns = patterns('sprints.views',
    url(r'^$', redirect_to, {'url': 'submit/'}),
    url(r'^submit/$', 'submit', name='submit'),
    url(r'^thankyou/$', 'thankyou', name='thankyou'),
)
