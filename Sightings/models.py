from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _

class squirrel(models.Model):

    Y = models.FloatField(
        help_text=_('Latitude'),
        max_length=100,
        blank = True,
        null = True,

        )

    X = models.FloatField(
        help_text=_('Longitude'),
        max_length=100,
        blank = True,
        null = True,
        )

    UniqueID = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=100,
        primary_key = True,
        )
    
    AM = 'AM'
    PM = 'PM'

    SHIFT_CH = (
    (AM, 'AM'),
    (PM, 'PM'),
    )

    Shift = models.CharField(
        max_length=20,
        choices = SHIFT_CH,
        blank = True 
        )

    Date = models.DateField(
        null = True,
        blank = True
    )

    Kit = 'Kitten'
    Ad = 'Adult'

    AGE_CH = (
    (Kit, 'Kitten'),
    (Ad, 'Adult')
    )

    Age = models.CharField(
        max_length=100,
        choices = AGE_CH,
        null = True,
    )

    GRAY = 'Gray'
    CIN = 'Cinnamon'

    FUR_CH = (
    (GRAY, 'Gray'),
    (CIN, 'Cinnamon'),
    )

    Fur = models.CharField(
        help_text=_('Primary Fur Color'),
        choices = FUR_CH,
        blank = True,
        max_length = 10,
    )

    Location = models.CharField(
        null = True,
        max_length=100,
        blank = True,
    )

    Spec_location = models.CharField(
        help_text=_('Location'),
        null = True,
        max_length=100,
    )

    Running = models.BooleanField(
    default = False,
    )

    Chasing = models.BooleanField(
    default = False,
    )

    Climbing = models.BooleanField(
    default = False,
    )

    Eating = models.BooleanField(
    default = False,
    )

    Foraging = models.BooleanField(
    default = False,
    )

    Other_activities = models.CharField(
    null = True,
    max_length=100,
    )

    Kuks = models.BooleanField(
    default = False,
    )

    Quaas = models.BooleanField(
    default = False,
    )

    Moans = models.BooleanField(
    default = False,
    )
    
    Tail_Flags = models.BooleanField(
    default = False,
    )

    Tail_Twitches = models.BooleanField(
    default = False,
    )

    Approaches = models.BooleanField(
    default =  False,
    )

    Indifferent = models.BooleanField(
    default = False,
    )

    Runs_From =models.BooleanField(
    default = False,
    )


   
