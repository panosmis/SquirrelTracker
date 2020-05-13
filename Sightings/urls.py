from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
        path('', views.sighting, name = 'sighting'),
        path('<UniqueID>/', views.update_sighting, name = 'update'),
        path('add/', views.add , name = 'add'),
        path('stats/', views.stats, name = 'stats'),
]

