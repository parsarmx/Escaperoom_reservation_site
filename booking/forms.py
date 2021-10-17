from django import forms
from .models import Player


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'last_name', 'number_of_players', 'phone', 'email', 'game')