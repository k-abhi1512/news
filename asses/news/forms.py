from django import forms
from .models import *
from django.forms import PasswordInput, FileInput


# This is the news inserting form
class InsertPageForm(forms.ModelForm):

    class Meta:
        model = InsertPage
        fields = '__all__'