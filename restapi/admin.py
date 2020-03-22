from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Drink, Beer, Shot, Snack, Beverage, Shop24H, Opinion, OpeningHours, Photo, PlaceReport, AddPlace
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


class PhotoAdmin(admin.ModelAdmin):
    #admin_image.allow_tags = True
    list_display = ('image_tag', 'is_checked')


class PlaceReportAdmin(admin.ModelAdmin):
    list_display = ('local_name', 'description', 'image_tag', 'signature', 'is_checked')


class PlaceAddAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'description', 'image_tag', 'signature', 'is_checked')

class AlcoholAdmin(admin.ModelAdmin):
    list_display = ('name', 'alcohol_places', 'price')
    search_fields = ('name', )
    filter_horizontal = ()

admin.site.register(AddPlace, PlaceAddAdmin)
admin.site.register(PlaceReport, PlaceReportAdmin)
admin.site.register(Photo, PhotoAdmin)
