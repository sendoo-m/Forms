from django import forms
from .models import Candidate
from django.core.validators import RegexValidator


class CandidateForm(forms.ModelForm):
    # validations
    firstname       = forms.CharField(
        label       ='First Name',max_length=50, 
        min_length  =3 ,
        validators  =[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message     ="only letters is allowed !")], 
        widget      =forms.TextInput(attrs={'placeholder':'First name'})
        )
    lastname        = forms.CharField(
        label       ='Last Name',max_length=50, 
        min_length  =3 ,
        validators  =[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message     ="only letters is allowed !")], 
        widget      =forms.TextInput(attrs={'placeholder':'Last name'})
        )
    email           = forms.EmailField(
        label       ='Email address', max_length=50, 
        min_length  =7,
        validators  =[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message     ="Put a valid email address !")], 
        widget      =forms.TextInput(attrs={'placeholder':'e-mail address'})
        )
    age           = forms.CharField(
        label       ='Your age', max_length=50, 
        min_length  =7,
        validators  =[RegexValidator(r'^[0-9]*$', 
        message     ="only number is allowd !")], 
        widget      =forms.TextInput(attrs={'placeholder':'Your age'})
        )
    class Meta:
        model       = Candidate
        fields      = '__all__'
        # fields      = ['firstname','lastname','age','email','message']
        # exclude      = ['firstname','lastname','age','email','message']