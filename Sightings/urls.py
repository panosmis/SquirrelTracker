from django.urls import path
from . import views

urlpatterns = [
        path('', views.sighting),
        path('<str:UniqueID/>',views.update_sighting),
        path('add/',views.add),
        path('stats/',views.stats),
        ]

