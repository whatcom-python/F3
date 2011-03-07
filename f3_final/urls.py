from django.conf.urls.defaults import patterns
from django.views.generic import list_detail

import views

urlpatterns = patterns('',
                       (r'^farms/$', views.farms_list),
                       (r'^farms/(?P<id>\d+)/$', views.farms_detail),
                       
                       (r'^farms/with/food/(?P<food_id>\d+)/$', views.farms_with_food),
                       (r'^food/$', views.food_list),
                       (r'^food/current$', views.food_current),
                       
                       (r'^$', views.index),
                       )

