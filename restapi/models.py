from django.db import models
from multiselectfield import MultiSelectField
from django.core.mail import send_mail
from random import randint
from django.db.models import Count
from django.conf import settings


WEEKDAYS = [
  (0, "Sunday"),  
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
]

DISTRICTS = [
    ("Śródmieście", "Śródmieście"),
    ("Mokotów", "Mokotów"),
    ("Ursynów", "Ursynów"),
    ("Wola", "Wola"),
    ("Bielany", "Bielany"),
    ("Praga Północ", "Praga Północ"),
    ("Praga Południe", "Praga Południe")
]


# class PlaceManager(models.Manager):
#     def random(self):
#         count = self.aggregate(count=Count('id'))['count']
#         random_index = randint(0, count - 1)
#         return self.all()[random_index]


class Place(models.Model):
    # objects = PlaceManager()
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50, choices=DISTRICTS)
    link = models.URLField(help_text="www.websiteurl.pl")
    additional_info = models.CharField(max_length=500, blank=True, null=True)
    is_updated = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        
    def report_place(self):
        self.is_updated = False
        self.save()


class OpeningHours(models.Model):
    place = models.ForeignKey("Place", on_delete=True, related_name = '%(class)s')
    week_day = models.IntegerField(choices=WEEKDAYS)
    open_hours = models.TimeField()
    close_hours = models.TimeField()

    def __str__(self):
        return str(self.place)+" "+str(self.week_day)+" "+str(self.open_hours)+" "+str(self.close_hours)

    class Meta:
        unique_together = ['place', 'week_day']
        ordering = ['week_day']
    # def get_weekday_from_display(self):
    #     return DAYS[self.weekday_from]

    # def get_weekday_to_display(self):
    #     return DAYS[self.weekday_to]



class Alcohol(models.Model):
    name = models.CharField(max_length=50)
    volume = models.FloatField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    additional_info = models.CharField(max_length=300, blank=True, null=True)
    place = models.ManyToManyField(Place, blank=False, related_name = '%(class)s')
    
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Drink(Alcohol):
    pass



class Shot(Alcohol):
    pass



class Beer(Alcohol):
    pass


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    additional_info = models.CharField(max_length=300, blank=True, null=True)
    place = models.ManyToManyField(Place, blank=False, related_name = 'beverage')
    
    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    additional_info = models.CharField(max_length=300, blank=True, null=True)
    place = models.ManyToManyField(Place, blank=False, related_name = 'snack')


class Shop24H(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50, choices=DISTRICTS)
    link = models.URLField(help_text="www.websiteurl.pl")
    week_day = MultiSelectField(choices=WEEKDAYS)
    additional_info = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Opinion(models.Model):
    opinion_text = models.TextField(max_length=1000)

    def send_email(self):
        subject = 'Opinion'
        message = self.opinion_text
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['jkszymans@gmail.com']
        # html_mes = 'to jest w html'
        send_mail(subject, message, from_email, recipient_list)


class Credits(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name