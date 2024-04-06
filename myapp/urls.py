from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="home"),
    path('main/',views.main1,name="main"),
    path('hacker/',views.main2,name="hacker"),
]
