from django.core.management.base import BaseCommand, CommandError
from f3_final.models import Farm
from geopy import geocoders
from sys import stdin

class Command( BaseCommand ):
    args = ''
    help = 'Sets latitude and longitude for all farms'

    def handle( self, *args, **options ):
        g = geocoders.Google()
        count = 0
        for farm in Farm.objects.all():
            count = count + 1
            if farm.longitude == None and farm.latitude == None:
                try:
                    place, ( lat, lng ) = g.geocode( farm.address + ', WA' )
                except:
                    pass
                else:
                    farm.address, farm.latitude, farm.longitude = place, lat, lng
                    farm.save()
        print count
