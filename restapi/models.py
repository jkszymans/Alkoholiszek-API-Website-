from django.db import models
from django.utils.safestring import mark_safe
from multiselectfield import MultiSelectField
from django.core.mail import send_mail
import calendar
from random import randint
from django.db.models import Count
from django.conf import settings


DAYS = [(day, day) for day in calendar.day_name]

HOUR_OF_DAY_24 = [(i,i) for i in range(1,25)]

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
    # open_hours = models.TimeField()
    # close_hours = models.TimeField()
    # week_day = MultiSelectField(choices=DAYS)
    additionalInfo = models.CharField(max_length=500, blank=True, null=True)
    is_updated = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        
    def report_place(self):
        self.is_updated = False
        self.save()


class OpeningHours(models.Model):
    place = models.ForeignKey("Place", on_delete=True, related_name = '%(class)s')
    week_day = models.CharField(choices=DAYS, max_length=50)
    open_hours = models.TimeField()
    close_hours = models.TimeField()
# input_formats=['%H:%M']
    class Meta:
        unique_together = ['place', 'week_day']
    # def get_weekday_from_display(self):
    #     return DAYS[self.weekday_from]

    # def get_weekday_to_display(self):
    #     return DAYS[self.weekday_to]


# class SpecialDays(models.Model):
#     holiday_date = models.DateField()
#     closed = models.BooleanField(default=True)
#     from_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24, null=True, blank=True)
#     to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24, null=True, blank=True)


class Alcohol(models.Model):
    name = models.CharField(max_length=50)
    volume = models.FloatField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    additionalInfo = models.CharField(max_length=300, blank=True, null=True)
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
    additionalInfo = models.CharField(max_length=300, blank=True, null=True)
    place = models.ManyToManyField(Place, blank=False, related_name = 'beverage')
    
    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    additionalInfo = models.CharField(max_length=300, blank=True, null=True)
    place = models.ManyToManyField(Place, blank=False, related_name = 'snack')


class Shop24H(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50, choices=DISTRICTS)
    link = models.URLField(help_text="www.websiteurl.pl")
    week_day = MultiSelectField(choices=DAYS)
    additionalInfo = models.CharField(max_length=500, blank=True, null=True)

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


class Photo(models.Model):
    name = models.TextField(max_length=30, default="Jazda")
    photo_img = models.ImageField(upload_to='images/', null=True)
    is_checked = models.BooleanField(default= False)

    def image_tag(self):
        if self.photo_img:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.photo_img.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class PlaceReport(models.Model):
    local_name = models.ForeignKey("Place",
                                    on_delete=models.CASCADE,
                                    related_name='%(class)s',
                                  )
    description = models.TextField(max_length=255)
    report_image = models.ImageField(null=True, upload_to='reports/')
    signature = models.CharField(max_length=20)
    is_checked = models.BooleanField(default= False)

    def image_tag(self):
        if self.report_image:
            return mark_safe('<img src="%s" style="width: 200px; height:200px;" />' % self.report_image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Report'

    def __str__(self):
        return self.description
