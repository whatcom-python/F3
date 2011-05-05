from django.contrib import admin

from f3_final import models

#admin.site.register(models.Farm)
admin.site.register(models.Food)
admin.site.register(models.ServiceOffering)
admin.site.register(models.PaymentMethod)
admin.site.register(models.FarmCategory)
admin.site.register(models.SustainabilityIndicator)

class FarmAdmin(admin.ModelAdmin):
    filter_horizontal = ('service_offerings','payment_methods','confirmed_foods'
        ,'sustainability_indicators','categories')
admin.site.register(models.Farm,FarmAdmin)
