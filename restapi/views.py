from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Place, Shot, Drink, Beer, Opinion, OpeningHours, Credits
from .serializers import PlaceDetailSerializer, PlaceListSerializer, OpinionSerializer, CreditsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter 
from django_filters import FilterSet
from django_filters import rest_framework as filters
import datetime
from django.db.models import F, Q
from random import randint
from django.db.models import Count


class PlaceFilter(FilterSet):
    district = filters.CharFilter('district')
    areThereDrinks = filters.BooleanFilter(field_name='drink', lookup_expr='isnull', exclude=True)
    areThereBeers = filters.BooleanFilter(field_name='beer', lookup_expr='isnull', exclude=True)
    areThereShots = filters.BooleanFilter(field_name='shot', lookup_expr='isnull', exclude=True)
    maxDrinkPrice = filters.NumberFilter(field_name='drink__price', lookup_expr='lte')
    maxShotPrice = filters.NumberFilter(field_name='shot__price', lookup_expr='lte')
    maxBeerPrice = filters.NumberFilter(field_name='beer__price', lookup_expr='lte')
    hasToBeOpenedRightNow = filters.BooleanFilter(method='hasToBeOpenedRightNowFilter')
    # openedAtGivenHour = filters.CharFilter(method='openedAtGivenHourFilter')


    class Meta:
        model = Place
        fields = ('district','areThereDrinks','areThereBeers',
        'areThereShots','maxDrinkPrice', 'maxBeerPrice',
        'maxShotPrice', 'hasToBeOpenedRightNow')
        # 'openedAtGivenHour')

    def hasToBeOpenedRightNowFilter(self, queryset, name, value):
        now = datetime.datetime.now()                                               
        current_day = int(now.strftime("%w"))                                        #current_day A
        current_time = now.time()                                               #current_time     
        x=1  
        if current_day=='Sunday':
            x=-6
        previous_day = str(int(now.strftime('%w'))-x)


        queryset_1 = OpeningHours.objects.filter(week_day = current_day)      #queryset filtered after current day
        queryset_2 = OpeningHours.objects.filter(week_day = previous_day)
        
        query_1 = queryset_1.filter(Q(open_hours__lt = current_time) & Q(close_hours__gt = current_time),open_hours__lt = F('close_hours'))              #queryset filtered after first condition       
        query_2 = queryset_1.filter(Q(open_hours__lt = current_time) & Q(open_hours__gt = F('close_hours')))                                      #queryset filtered after second condition
        query_merged = query_1 | query_2

        query_3 = queryset_2.filter(Q(close_hours__gt = current_time) & Q(open_hours__gt = F('close_hours')))
        
        
        queryset_filtered = query_merged | query_3                            #merge two querysets with time conditions
        if not value:
            queryset = queryset.exclude(openinghours__in=queryset_filtered)
        else:
            queryset = queryset.filter(openinghours__in=queryset_filtered)
        return queryset


    # def openedAtGivenHour(self, queryset, name, value):
    #     pass

class PlaceList(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    filter_class = PlaceFilter

    def get_queryset(self):
        queryset = Place.objects.all()
        return queryset



class PlaceDetail(generics.RetrieveAPIView):
    serializer_class = PlaceDetailSerializer
    queryset = Place.objects.all()



@api_view(['GET'])
def place_random(request, format=None):
    district = request.GET.get('district', None)
    place = Place.objects.all()
    if district is not None:
        place = place.filter(district=district)
    if request.method == 'GET':
        count = place.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        place = place.all()[random_index]
        serializer = PlaceListSerializer(place)
        return Response(serializer.data)


@api_view(['GET','POST'])
def opinion(request, format=None):
    if request.method == 'GET':
        opinion_query = Opinion.objects.all()
        serializer = OpinionSerializer(opinion_query,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OpinionSerializer(data=request.data)
        if serializer.is_valid():
            inst = serializer.save()
            inst.send_email()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def report_place(request,format=None):
    id = request.GET.get('id', None)
    if id:
        place = Place.objects.get(id=id)
        place.is_updated = False
        place.save()
        serializer = PlaceDetailSerializer(place)
        return Response(serializer.data)


class CreditsList(generics.ListCreateAPIView):
    queryset = Credits.objects.all()
    serializer_class = CreditsSerializer



        
# @api_view(['GET', 'POST'])
# def place_list(request, format=None):
#     if request.method == 'GET':
#         place = Place.objects.all()
#         serializer = PlaceListSerializer(place, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PlaceListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def place_detail(request, id, format=None):
#     try:
#         place = Place.objects.get(id=id)

#     except Place.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PlaceDetailSerializer(place)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PlaceDetailSerializer(place, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         place.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)