from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django import forms
from django.urls import reverse_lazy 
from .models import squirrel
from .forms import SquirrelForm
import json
import random

def sighting(request):
    squirrels = squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/sight.html', context)


def update_sighting(request, UniqueID):
    form = SquirrelForm(instance=squirrel)
    context={
            'form':form,
            'squirrel':squirrel
    }
    return render(request,'sightings/update.html', context)




def add():

    form = SquirrelForm()
    context = {'form': form,}
    return render(request, 'sightings/add.html', context)


def stats(request):
    num_squirrels = squirrel.objects.all().count()
    old_squirrels = squirrel.objects.filter(Age = 'Adult').count()
    cin_fur = squirrel.objects.filter(Fur = 'Cinnamon').count()
    gray_fur = squirrel.objects.filter(Fur = 'Gray').count()
    squirrel_moan = squirrel.objects.filter(Moans = 'TRUE').count()
    twitchin_squirrel = squirrel.objects.filter(Tail_twitches = 'TRUE').count()

    context = {
            'num_squirrels': num_squirrels,
            'old_squirrels': old_squirrels,
            'cin_fur': cin_fur,
            'gray_fur': gray_fur,
            'squirrel_moan': squirrel_moan,
            'twitchin_squirrel': twitchin_squirrel
            }
    return render(request, 'sightings/stats.html',context)

def map (request):
    Squirrels = squirrel.objects.all()[:100]
    context = {
            'Squirrels': Squirrels
            }
    return render (request, 'sightings/map.html', context)
