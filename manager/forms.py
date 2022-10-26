from django import forms
from .models import Passwords

class PasswordsForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = "__all__"

class NewPasswordsForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = "__all__"