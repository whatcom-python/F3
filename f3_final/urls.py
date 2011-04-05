from django.conf.urls.defaults import patterns, url
from django.views.generic import list_detail

import views

urlpatterns = patterns('',
                       url(r'^farms/$', views.farms_list, name="farms_list"),
                       url(r'^farms/(?P<id>\d+)/$', views.farms_detail, name="farms_detail"),

                       url(r'^farms/with/food/(?P<food_id>\d+)/$', views.farms_with_food, name="farms_with_food"),
                       url(r'^food/$', views.food_list, name="food_list"),
                       url(r'^food/current$', views.food_current, name="food_current"),

                       url(r'^$', views.index, name="index"),
                       )

