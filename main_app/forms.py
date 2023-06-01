# forms.py

from django.forms import ModelForm
from .models import Worn

class WornForm(ModelForm):
  class Meta:
    model = Worn
    fields = ['date', 'usage']