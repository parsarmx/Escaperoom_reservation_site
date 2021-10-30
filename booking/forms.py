from django import forms
from .models import Player


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'last_name', 'number_of_players', 'phone', 'email', 'game')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'نام'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی'
        self.fields['number_of_players'].widget.attrs['placeholder'] = 'تعداد بازیکنان'
        self.fields['phone'].widget.attrs['placeholder'] = 'شماره موبایل'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'

    def clean_phone(self):
        phone = self.cleaned_data['phone'].replace(" ", "")
        return phone
