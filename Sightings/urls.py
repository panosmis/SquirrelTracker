from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
        path('sightings/', views.sighting, name = 'sighting'),
        path('sightings/<UniqueID>/', views.update_sighting, name = 'update'),
        path('sightings/add/', views.add , name = 'add'),
        path('sightings/stats/', views.stats, name = 'stats'),
        path('map/', views.map, name = 'map'),
        ]

