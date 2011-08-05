import django.db.models as m


class Farm(m.Model):

    name = m.CharField(max_length=100)
    contact_person = m.CharField(max_length=100)
    address = m.TextField()
    latitude = m.FloatField(null=True,blank=True)
    longitude = m.FloatField(null=True,blank=True)
    phone_number = m.CharField(max_length=30)
    website = m.URLField(blank=True)
    email_address = m.EmailField(blank=True)
    description = m.TextField(blank=True)
    hours_of_operation = m.CharField(max_length=100,blank=True)
    seasonal_operation = m.CharField(max_length=100,blank=True)
    service_offerings = m.ManyToManyField('ServiceOffering',blank=True)
    payment_methods = m.ManyToManyField('PaymentMethod',blank=True)
    sustainability_indicators = m.ManyToManyField('SustainabilityIndicator',blank=True)
    categories = m.ManyToManyField('FarmCategory',blank=True)
    confirmed_foods = m.ManyToManyField('Food',blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/f3/farms/%s/" % self.id

    def get_service_offerings(self):
        service_list = []
        for service in self.service_offerings.all():
            service_list.append(service.name)
        return service_list

    def acceptscreditcards(self):
        if self.payment_methods.all():
            for payment in self.payment_methods.all():
                if payment.name in ["Visa","MC"]:
                    return True

    def displaydescription(self):
        return "Located at:" + self.address or '???'

    class Meta:
        ordering = ["name"]


class FarmCategory(m.Model):

    name = m.CharField(max_length=50)
    foods = m.ManyToManyField('Food')

    class Meta:
        verbose_name_plural = 'farm categories'

    def __unicode__(self):
        return self.name


class Food(m.Model):
    """Some food that grows on a farm."""

    name = m.CharField(max_length=50,
                       unique=True,
                       help_text="the name of the food")
    type = m.ForeignKey('FoodType')
    months = m.ManyToManyField('Month')
    description = m.TextField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/f3/food/%s/" % self.name

    def displaydescription(self):
        return self.type

    class Meta:
        ordering = ["name"]


class FoodType(m.Model):

    name = m.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name


class Month(m.Model):
    """The months"""

    name = m.CharField(max_length=10,
                       unique=True,
                       help_text="the month")
    order = m.IntegerField(unique=True)

    def __unicode__(self):
        return self.name


class PaymentMethod(m.Model):
    """How you can pay for the food. Includes a 'null value' of
    Unspecified, since we expect our knowledge is incomplete."""
    name = m.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class ServiceOffering(m.Model):
    """Services offered by a Farm (e.g. U-Pick, Phone Orders)"""
    name = m.CharField(max_length=50, unique=True)
    description = m.TextField(blank=True)

    def __unicode__(self):
        return self.name


class SustainabilityIndicator(m.Model):
    """Commitments by a Farm to sustainability. Represented by an icon
    in the paper guide. There are likely some inter-relationships here
    we're not modeling."""
    name = m.CharField(max_length=50, unique=True)
    description = m.TextField()
    filename_base = m.CharField(max_length=50)

    def __unicode__(self):
        return self.name
