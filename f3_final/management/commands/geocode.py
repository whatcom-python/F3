from django.core.management.base import BaseCommand, CommandError
from f3_final.models import Farm
from geopy import geocoders

class Command( BaseCommand ):
    args = ''
    help = 'Sets latitude and longitude for all farms'

    def handle( self, *args, **options ):
        g = geocoders.Google()
        count = 0
        for farm in Farm.objects.all():
            if farm.address != "":
                count = count + 1
                if farm.longitude == None and farm.latitude == None:
                    try:
                        place, ( lat, lng ) = g.geocode( farm.address + ', WA' )
                    except:
                        raise CommandError, "There was a error getting an lat/long pair for farm" % ( farm.name )
                    else:
                        print "I think farm \"%s\" is at latitude \"%s\", longitude \"%s\"" % (farm.name, lat, lng)
                        farm.address, farm.latitude, farm.longitude = place, lat, lng
                        farm.save()
        print "Added latitude and longitude to %s farms." % (count)
