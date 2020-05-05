from django.forms import ModelForm
from .models import squirrel

class SightForm(ModelForm):
    class Meta:

        model = squirrel
        fields = '__all__'


