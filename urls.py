from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import f3_final.views

urlpatterns = patterns('',


                       # dispatch to the urls for f3_final
                       (r'^f3/', include('f3.f3_final.urls')),

                       # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
                       # to INSTALLED_APPS to enable admin documentation:
                       # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       #(r'^admin/', include(admin.site.urls)),
                       )
