from django.urls import path, re_path
from mysite import views

app_name = "mysite"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.CreatePlaceView.as_view(), name='register'),
    path('credits', views.credits_view, name='credits'),
    path('about', views.about_view, name='about'),
]