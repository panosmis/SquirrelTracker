from django.shortcuts import render
from django.http import HttpResponse

from .models import squirrel
from .forms import SightForm

def sighting(request):
    squirrels = squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'Sightings/sight.html', context)


def update_sighting(request, UniqueID):
    squirrels = squirrel.objects.get(UniqueID = UniqueID)
    form = SightForm
    context = {
            'form':form,
            }
    return render(request,'Sightings/update.html', context)




def add():
    form = FORM(request.POST)
    if form.is_valid():
        context = {'form': form,}
        return render(request, 'Sightings/add.html', context)


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
    return render(request, 'Sightings/stats.html',context)

def map (request):
    Squirrels = squirrel.objects.all()[:100]
    context = {
            'Squirrels': Squirrels
            }
    return render (request, 'Sightings/map.html', context)
