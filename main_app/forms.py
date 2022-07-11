from django.forms import ModelForm
from .models import Doing

class DoingForm(ModelForm):
    class Meta:
        model = Doing
        fields = ['date', 'time']