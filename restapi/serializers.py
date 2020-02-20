from .models import Place, Drink, Shot, Beer, Opinion, Credits, OpeningHours
from rest_framework import serializers
from django.core.mail import send_mail



class PlaceDetailSerializer(serializers.ModelSerializer):
    drinks = serializers.SerializerMethodField('get_drink_data')
    beers = serializers.SerializerMethodField('get_beer_data')
    shots = serializers.SerializerMethodField('get_shot_data')
    beverages = serializers.SerializerMethodField('get_beverage_data')
    snacks = serializers.SerializerMethodField('get_snack_data')
    open_close_hours = serializers.SerializerMethodField('get_open_close_hours')
    class Meta:
        model = Place
        fields = ('id','name', 'lat', 'lng', 'address', 'district', 'link',
         'additional_info', 'drinks', 'beers', 'shots', 'beverages', 'snacks',
          'open_close_hours')

    def get_drink_data(self, plaace):
        drinks = plaace.drink.values('name', 'volume', 'percentage', 'price', 'additional_info')
        return drinks

    def get_beer_data(self, plaace):
        beers = plaace.beer.values('name', 'volume', 'percentage', 'price', 'additional_info')
        return beers

    def get_shot_data(self, plaace):
        shots = plaace.shot.values('name', 'volume', 'percentage', 'price', 'additional_info')
        return shots

    def get_beverage_data(self, plaace):
        beverages = plaace.beverage.values('name', 'volume', 'price', 'additional_info')
        return beverages

    def get_snack_data(self, plaace):
        snacks = plaace.snack.values('name', 'price', 'additional_info')
        return snacks

    def get_open_close_hours(self, plaace):
        hours = plaace.openinghours.values('week_day','open_hours','close_hours')
        return hours


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'address', 'lat', 'lng')


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'
    
class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credits
        fields = '__all__'

