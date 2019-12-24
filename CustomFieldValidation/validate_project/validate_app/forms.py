from django import forms
from .models import CustomModel
from .validate import validate_email,zip_validator
class CustomForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_email,],widget=forms.EmailInput(attrs={
        'class':'input',
        'id':'pass',
    }))

    username = forms.CharField(validators=[],widget=forms.TextInput(attrs={
        'class':'input',
        'id':'user',
    }))

    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'input',
        'id':'pass',

    }))

    check = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'id':'check',

    }))

    zip = forms.CharField(validators=[zip_validator],widget=forms.TextInput(attrs={
        'class':'input',
        'id':'user',
    }))

    class Meta:
        model = CustomModel
        fields= [
        'username',
        'email',
        'password',
        'zip',
        'check',

        ]

    # def clean(self):
