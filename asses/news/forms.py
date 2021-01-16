from django import forms
from .models import *


class InsertPageForm(forms.ModelForm):

    class Meta:
        model = InsertPage
        fields = '__all__'