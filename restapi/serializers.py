from .models import Place, Drink, Shot, Beer, Opinion, Photo
from rest_framework import serializers
from django.core.mail import send_mail
# class DrinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Drink
#         fields = ('name', 'volume', 'percentage', 'price', 'additionalInfo')


# class ShotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shot
#         fields = ('name', 'volume', 'percentage', 'price', 'additionalInfo')


# class BeerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Beer
#         fields = ('name', 'volume', 'percentage', 'price', 'additionalInfo')


class PlaceDetailSerializer(serializers.ModelSerializer):
    drinks = serializers.SerializerMethodField('get_drink_data')
    beers = serializers.SerializerMethodField('get_beer_data')
    shots = serializers.SerializerMethodField('get_shot_data')
    beverages = serializers.SerializerMethodField('get_beverage_data')
    snacks = serializers.SerializerMethodField('get_snack_data')
    class Meta:
        model = Place
        fields = ('name', 'lat', 'lng', 'address', 'district', 'link',
         'additionalInfo', 'drinks', 'beers', 'shots', 'beverages', 'snacks')

    def get_drink_data(self, plaace):
        drinks = plaace.drink.values('name', 'volume', 'percentage', 'price', 'additionalInfo')
        return drinks

    def get_beer_data(self, plaace):
        beers = plaace.beer.values('name', 'volume', 'percentage', 'price', 'additionalInfo')
        return beers

    def get_shot_data(self, plaace):
        shots = plaace.shot.values('name', 'volume', 'percentage', 'price', 'additionalInfo')
        return shots

    def get_beverage_data(self, plaace):
        beverages = plaace.beverage.values('name', 'volume', 'price', 'additionalInfo')
        return beverages

    def get_snack_data(self, plaace):
        snacks = plaace.snack.values('name', 'price', 'additionalInfo')
        return snacks


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'address', 'lat', 'lng')


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

