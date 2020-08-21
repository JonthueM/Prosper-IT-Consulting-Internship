from django import forms
from django.forms import ModelForm
from .models import Games_UpComing




class GamesUpComingForm(ModelForm):
    class Meta:
        model = Games_UpComing
        fields = '__all__'


