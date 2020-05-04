from django.db import models

from django.utils.translation import gettext as _

class squirrel(models.Model):
    Latitude = models.FloatField(
        help_text=_('Latitude'),
        max_length=100,
        )

    Longitude = models.FloatField(
        help_text=_('Longitude'),
        max_length=100,
        )

     UniqueID = models.CharField(
        help_text_('Longitude'),
        max_length=100,
        )


