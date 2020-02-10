from django.contrib import admin
from .models import Place, Drink, Beer, Shot, Snack, Beverage, Shop24H, Opinion, OpeningHours
admin.site.register(Drink)
admin.site.register(Beer)
admin.site.register(Shot)
admin.site.register(Place)
admin.site.register(Snack)
admin.site.register(Beverage)
admin.site.register(Shop24H)
admin.site.register(Opinion)
admin.site.register(OpeningHours)
# admin.site.register(SpecialDays)