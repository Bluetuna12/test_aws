from django.contrib import admin
from django.urls import path

from . import views

app_name = 'pepp'
urlpatterns = [
    path('', views.home, name='home'),
    path('2004', views.M2004, name='m2004'),
    path('2005', views.M2005, name='m2005'),
    path('2006', views.M2006, name='m2006'),
    path('2007', views.M2007, name='m2007'),
    path('2008', views.M2008, name='m2008'),
    path('2009', views.M2009, name='m2009'),
    path('2010', views.M2010, name='m2010'),
    path('2011', views.M2011, name='m2011'),
    path('2012', views.M2012, name='m2012'),
    path('2013', views.M2013, name='m2013'),
    path('2014', views.M2014, name='m2014'),
    path('2015', views.M2015, name='m2015'),
    path('2016', views.M2016, name='m2016'),
    path('2017', views.M2017, name='m2017'),
    path('2018', views.M2018, name='m2018'),
    path('2019', views.M2019, name='m2019'),
    path('2020', views.M2020, name='m2020'),
    path('2021', views.M2021, name='m2021'),
]