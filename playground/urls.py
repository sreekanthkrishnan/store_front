from django.urls import path
from . import views

#URLCONFIG
urlpatterns =[
    path('store/',views.say_hello)
]