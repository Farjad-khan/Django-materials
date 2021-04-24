from django.core import validators
from django import forms
from .models import User



class StudentRegistration(forms.ModelForm):
  #name  = forms.CharField(max_length=50, required=False)
  class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels={'name':'Enter Name','email':'Enter Email','password' : 'Enter password' }
       
        widgets = {
            'password': forms.PasswordInput
            }
        


#It was all about the customization of django Modelforms, hope you got understand
