import datetime

try:
    import json
except ImportError:
    import simplejson as json

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.template.loader import get_template
import f3_final.models as models

def index( request ):
    return render_to_response( "index.html",
                              {}, context_instance = RequestContext( request ) )


def farms_list( request ):
    obj_list = models.Farm.objects.all()
    return render_to_response( 'object_list.html',
                               {'object_list': obj_list,
                                'object_type': 'Farm',
                                }, context_instance = RequestContext( request ) )


def farms_detail( request, id ):
    obj = get_object_or_404( models.Farm, id = id )
    return render_to_response( 'farm_detail.html',
                               {'object':obj,
                                'object_type':'Farm',
<<<<<<< HEAD
                                },context_instance=RequestContext(request))
=======
                                }, context_instance = RequestContext( request ) )
    #return HttpResponse("<html><body>Farm %s is called %s</body></html>" %
    #                    (obj.id, obj.name))
>>>>>>> dd84ade4bff83b13189bf216a2947946ff654cd8


def food_list( request ):
    obj_list = models.Food.objects.all()
    return render_to_response( 'object_list.html',
                              {'object_list': obj_list,
                               'object_type': 'Food',
                               }, context_instance = RequestContext( request ) )


def food_current( request ):
    thismonth = datetime.datetime.now().month
    obj_list = get_list_or_404( models.Food, months = thismonth )
    restr = ' (month of %s)' % models.Month.objects.get( id = thismonth ).name
    return render_to_response( 'object_list.html',
                              {'object_list': obj_list,
                               'object_type': 'Food',
                               'restriction': restr,
                               }, context_instance = RequestContext( request ) )


<<<<<<< HEAD
def food_detail(request, name):
    obj = get_object_or_404(models.Food, name=name)
    return render_to_response('food_detail.html',
                               {'object':obj,
                                'object_type':'Food',
                                },context_instance=RequestContext(request))


def farms_with_food(request, food_id):
    obj_list = get_list_or_404(models.Farm, confirmed_foods=food_id)
    restr = ' (with %s)' % models.Food.objects.get(id=food_id).name
    return render_to_response('object_list.html',
=======
def farms_with_food( request, food_id ):
    obj_list = get_list_or_404( models.Farm, confirmed_foods = food_id )
    restr = ' (with %s)' % models.Food.objects.get( id = food_id ).name
    return render_to_response( 'object_list.html',
>>>>>>> dd84ade4bff83b13189bf216a2947946ff654cd8
                              {'object_list': obj_list,
                               'object_type': 'Farm',
                               'restriction': restr,
                               }, context_instance = RequestContext( request ) )

def farm_json_for_map( request ):
    return HttpResponse( 
                        json.dumps( 
                                   [
                                       [
                                        farm.name,
                                        [
                                         farm.latitude,
                                         farm.longitude
                                        ]
                                       ]
                                      for farm in models.Farm.objects.all()
                                    ],
                                    indent = 4,
                                    sort_keys = True
                                )
                            )
