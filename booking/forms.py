from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    number_of_players = forms.IntegerField()
