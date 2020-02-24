from django.urls import path
from register import views

app_name = "register"

urlpatterns = [
    path('user_register/', views.user_register, name='user-register'),
]