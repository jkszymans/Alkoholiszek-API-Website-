from django.urls import path, re_path
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.PlaceList.as_view(), name='place_list'),
    path('<int:pk>/', views.PlaceDetail.as_view(), name='place_detail'),
    path('random/', views.place_random, name='place_random_filtered'),
    path('opinion/',views.opinion, name='opinion'),
    path('report-place/', views.report_place, name='report_place')   
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','html'])