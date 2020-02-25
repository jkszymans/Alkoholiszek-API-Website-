from django.urls import path, re_path
from restapi import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.PlaceList.as_view(), name='place_list'),
    path('<int:pk>/', views.PlaceDetail.as_view(), name='place_detail'),
    path('random/', views.place_random, name='place_random_filtered'),
    path('opinion/',views.opinion, name='opinion'),
    path('credits', views.CreditsList.as_view(), name='credits_list'),
    path('images/', views.PhotoUploadView.as_view()),
    path('images/all/', views.PhotoList, name='list'),
    path('report-place/', views.ReportPlaceView.as_view()),
    path('submit-place/', views.PlaceSubmitView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','html'])

