from django.urls import path
from . import views

urlpatterns = [
        path('', views.sighting, name = 'all squirrels'),
        path('<str:UniqueID>/', views.update_sighting, name = 'update'),
        path('add/', views.add , name = 'add'),
        path('stats/', views.stats, name = 'stats'),
        path('map/', views.map, name = 'map'),
        ]

