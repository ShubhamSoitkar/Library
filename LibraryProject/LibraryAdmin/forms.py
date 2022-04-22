import imp
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LibraryAdminForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput(), label='CONFIRM PASSWORD')
    class Meta:
        model = CustomUser
        fields = ['user_name','email','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

        labels = {
            'user_name': 'USERNAME',
            'email': 'Email Id',
            'password': 'PASSWORD',
        }
    def clean(self):
        all_data = super().clean()
        print(all_data)
        pass1 = all_data.get('password')
        pass2 = all_data.get('confirm_password')
        if pass1 != pass2 :
            raise forms.ValidationError('Password does not match')