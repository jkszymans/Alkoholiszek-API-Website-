from django.forms import ModelForm
from restapi import models


class PlaceForm(ModelForm):
    class Meta:
        model = models.Place
        fields = '__all__'