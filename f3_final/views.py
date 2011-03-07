import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

import f3_final.models as models

def index(request):
    return HttpResponse('this is the Hello world from f3')


def farms_list(request):
    obj_list = models.Farm.objects.all()
    return render_to_response('myfirsttemplate.html',
                              {'object_list': obj_list,
                               'object_type': 'Farm',
                               })
#     return render_to_response('object_list.html',
#                               {'object_list': obj_list,
#                                'object_type': 'Farm',
#                                })


def farms_detail(request, id):
    obj = get_object_or_404(models.Farm, id=id)
    return HttpResponse("<html><body>Farm %s is called %s</body></html>" %
                        (obj.id, obj.name))


def food_list(request):
    obj_list = models.Food.objects.all()
    return render_to_response('object_list.html',
                              {'object_list': obj_list,
                               'object_type': 'Food',
                               })

    
def food_current(request):
    thismonth = datetime.datetime.now().month
    obj_list = get_list_or_404(models.Food, months=thismonth)
    restr = ' (month of %s)' % models.Month.objects.get(id=thismonth).name
    return render_to_response('object_list.html',
                              {'object_list': obj_list,
                               'object_type': 'Food',
                               'restriction': restr,
                               })

    
def farms_with_food(request, food_id):
    obj_list = get_list_or_404(models.Farm, confirmed_foods=food_id)
    restr = ' (with %s)' % models.Food.objects.get(id=food_id).name
    return render_to_response('object_list.html',
                              {'object_list': obj_list,
                               'object_type': 'Farm',
                               'restriction': restr,
                               })
