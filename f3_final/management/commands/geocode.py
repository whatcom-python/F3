from django.core.management.base import BaseCommand, CommandError
from f3_final.models import Farm
from geopy import geocoders

class Command( BaseCommand ):
    args = ''
    help = 'Sets latitude and longitude for all farms with an address.'

    def handle( self, *args, **options ):
        g = geocoders.Google()
        count = 0
        errors = []
        for farm in Farm.objects.all():
            if farm.address != "":

                if farm.longitude == None and farm.latitude == None:
                    try:
                        place, ( lat, lng ) = g.geocode( farm.address + ', WA' )
                    except:
                        print "There was a error getting an lat/long pair for farm %s" % ( farm.name )
                        errors.append(farm.name)
                    else:
                        print "Farm \"%s\" is at latitude \"%s\", longitude \"%s\"" % ( farm.name, lat, lng )
                        farm.address, farm.latitude, farm.longitude = place, lat, lng
                        farm.save()
                        count = count + 1
        print "Added latitude and longitude to %i farms with %i errors." % ( count, len(errors) )
