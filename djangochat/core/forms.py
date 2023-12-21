from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from core.models import CustomUser
from django.contrib.auth import get_user_model

class SignUpForm(forms.ModelForm):
    username =forms.CharField(label = 'Username ', max_length = 25)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    # User=get_user_model()
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password don't match")
        return password2

