from django import forms
from .models import List, Item
from django.contrib.auth.forms import AuthenticationForm



class CreateListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', max_length=100)

class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['text']