from django.contrib import admin
from .models import Place, Drink, Beer, Shot, Snack, Beverage, Shop24H, Opinion, OpeningHours, Credits, Photo, PlaceReport
from django.utils.safestring import mark_safe

admin.site.register(Drink)
admin.site.register(Beer)
admin.site.register(Shot)
admin.site.register(Place)
admin.site.register(Snack)
admin.site.register(Beverage)
admin.site.register(Shop24H)
admin.site.register(Opinion)
admin.site.register(OpeningHours)
admin.site.register(Credits)


class PhotoAdmin(admin.ModelAdmin):
    #admin_image.allow_tags = True
    list_display = ('name', 'image_tag')


class PlaceReportAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'description', 'photo_id_list', 'signature', 'is_checked')


admin.site.register(PlaceReport, PlaceReportAdmin)
admin.site.register(Photo, PhotoAdmin)

