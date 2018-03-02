from django import forms
from .models import Proverb

class ProverbForm(forms.ModelForm):
    class Meta:
        model = Proverb
        fields = ['proverb']
