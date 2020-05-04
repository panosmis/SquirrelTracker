from django.db import models
from django.utils.translation import gettext as _


class Sighting(models.Model):

    X = models.FloatField(
            help_text=_('Long'),
            max_length= 200, default= 0.0,)
    Y = models.FloatField(
            help_text=_('Lat'),
            max_length= 200, default= 0.0,)
    unique_squirrel_id = models.CharField(
            help_text=_('Squirel Id'),
            max_lenght=15,
            primary_key=True,)
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
            (AM,'AM'),
            (PM,'PM'),
            )
    Shift = models.CharField(
        choices = SHIFT_CHOICES,
        max_lenght = 2,)

    date = models.DateField(
            )


