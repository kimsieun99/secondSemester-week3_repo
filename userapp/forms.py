from .models import User
from django.contrib.auth import forms

class CustomUser(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nickname']