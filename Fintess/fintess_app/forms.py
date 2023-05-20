from django import forms
from .models import InputValue

class InputForm(forms.ModelForm):
    class Meta:
        model = InputValue
        fields = ['value']