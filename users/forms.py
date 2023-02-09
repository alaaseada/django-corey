from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name', max_length=20, widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField(label='Last Name', max_length=20)

    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
