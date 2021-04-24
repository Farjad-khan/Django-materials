from django.core import validators
from django import forms
from .models import User



class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels={'name':'Enter Name','email':'Enter Email','password' : 'Enter password' }
        error_messages = {
            'name':{'required':'Name is required'},
            'password':{'required':'Password is required'}
          }
        widgets = {
            'password': forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'Enter Name'})
            }


#It was all about the customization of django forms, hope you got understand
