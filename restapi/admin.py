from django.contrib import admin
from .models import *
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


# class PhotoAdmin(admin.ModelAdmin):
#     #admin_image.allow_tags = True
#     list_display = ('image_tag',)


# class PlaceReportAdmin(admin.ModelAdmin):
#     list_display = ('place', 'description', 'photo_id_list', 'signature', 'is_checked')


admin.site.register(PlaceReport)
admin.site.register(Photo)
admin.site.register(PlaceSubmit)

