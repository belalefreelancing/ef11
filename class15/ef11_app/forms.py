from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name']
        # exclude = ('name',)


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=200)
#     email = forms.EmailField()

