from django.conf.urls.defaults import *
from django.conf import settings
from nbio.django.views import auto
import sarahpalin.views as views


HOST = 'host'
PATH = 'path'
LOCATION = 'location'
APP_HOST = settings.HOSTS['app']
STATIC_HOST = settings.HOSTS['static']


urlpatterns = patterns('',
    (r'^$', views.home, {HOST: APP_HOST}),
    (r'^home/?$', auto, {HOST: APP_HOST, PATH: '/'}),
        
    (r'^cee-dub/?$', auto, {LOCATION: 'http://cee-dub.info/'}),
    (r'^rk/?$', auto, {LOCATION: 'http://theryanking.com/'}),
    (r'^case/?$', auto, {LOCATION: 'http://vedana.net/'}),
    (r'^ydnar/?$', auto, {LOCATION: 'http://ydnar.com/'}),
    (r'^blog/?$', auto, {LOCATION: 'http://blog.sarahpalinisjohnmccainsnewbicycle.com/'}),
    (r'^help/?$', auto, {LOCATION: 'http://getsatisfaction.com/sarahpalinisjohnmccainsnewbicycle'}),
        
    (r'.*', auto, {HOST: APP_HOST}),
)
