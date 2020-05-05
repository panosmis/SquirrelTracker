from django.shortcuts import render
from django.http import HttpResponse

from .models import squirrel
from .forms import SightForm

def siqhting(request):
    squirrels = squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'Sightings/sight.html', context)


def update_sighting(request, UniqueID):
    squirrel = squirrel.objects.get(UniqueID = UniqueID)
    form = SightForm
    context = {
            'form':form,
            }
    return render(request,'Sightings/update.html', context)




def add():

    return 'To be filled'


def stats():

    return 'To be filled'

def map():

    return "Should map be here though?"


