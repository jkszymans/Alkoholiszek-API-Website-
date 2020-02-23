from django.contrib import admin
<<<<<<< HEAD
from .models import Place, Drink, Beer, Shot, Snack, Beverage, Shop24H, Opinion, OpeningHours, Credits
=======
from django.utils.safestring import mark_safe

from .models import Place, Drink, Beer, Shot, Snack, Beverage, Shop24H, Opinion, OpeningHours, Photo, PlaceReport
>>>>>>> c7ddbfdd6c52decb9671349bd51d1c8bb2b0b334
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
    list_display = ('name', 'image_tag', 'is_checked')


class PlaceReportAdmin(admin.ModelAdmin):
    list_display = ('local_name', 'description', 'image_tag', 'signature', 'is_checked')


admin.site.register(PlaceReport, PlaceReportAdmin)
admin.site.register(Photo, PhotoAdmin)

