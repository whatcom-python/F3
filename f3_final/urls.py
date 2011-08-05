from django.conf.urls.defaults import patterns, url, include
from django.views.generic import list_detail
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns( '',
                       url( r'^farm/(?P<id>\d+)/$', views.farms_detail,
                           name = "farm_detail" ),

                       url(r'^food/(?P<id>\d+)/$', views.food_detail,
                           name="food_detail"),

                       url( r'^json/all',
                           "f3_final.views.farm_json_all" ),

                       url( r'^$', views.index, name = "index" ),
                       #url( r'^admin/', include( admin.site.urls ) )

                       )

# Django's static file server is inefficient and insecure
# for production use, serve these files via Apache or (better) Nginx
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
 )
