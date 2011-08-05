import f3_final.models as models
import datetime, calendar

named_month = lambda month_num:calendar.month_name[month_num]

def menu(request):
    thisMonth = datetime.datetime.now().month
    currentFoods = models.Food.objects.filter( months = thisMonth )
    otherFoods = models.Food.objects.exclude( months = thisMonth )
    farms = models.Farm.objects.all()
    return {
        'currentFoods': currentFoods,
        'otherFoods': otherFoods,
        'farms': farms
    }