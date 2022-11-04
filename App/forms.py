from tkinter import Widget
from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

# Every letters to LowerCase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
# Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

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
    job           = Uppercase(
        label       ='Job Code', max_length=7, 
        min_length  =7,
        
        widget      =forms.TextInput(attrs={'placeholder':'Example FR-221'})
        )
    email           = Lowercase(
        label       ='Email address', max_length=50, 
        min_length  =7,
        validators  =[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message     ="Put a valid email address !")], 
        widget      =forms.TextInput(attrs={'placeholder':'e-mail address'})
        )
    age           = forms.CharField(
        label       ='Your age', max_length=50, 
        min_length  =1,
        validators  =[RegexValidator(r'^[0-9]*$', 
        message     ="only number is allowd !")], 
        widget      =forms.TextInput(attrs={'placeholder':'Your age'})
        )
    
    class Meta:
        model       = Candidate
        # fields      = '__all__'
        # fields      = ['firstname','lastname','age','email','message']
        exclude      = ['situation','created-at']

        SALARY   = (
            ('','salary expectation (month)'),
            ('Between ($3000 and $4000 )','Between ($3000 and $4000 )'),
            ('Between ($4000 and $5000 )','Between ($4000 and $5000 )'),
            ('Between ($5000 and $7000 )','Between ($5000 and $7000 )'),
            ('Between ($7000 and $10000 )','Between ($7000 and $10000 )')
        )

        # Method 2
        GENDER = [('M','Male'),('F','Female')]

        # Method 2
        SMOKER = [('1','Yes'),('2','No')]
        # OUR WIDGETS

        widgets = {
            # Phone
            'Phone': forms.TextInput(
                attrs={
                'style':'font-size: 1rem',
                'placeholder':'phone',
                'data-mask':'(00) 00000-0000'
                }
            ),

            # salary
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                'class':'form-control', # Bootstrap inside the forms.py
                
                }
            ),

            # gender
            'gender': forms.RadioSelect(
                choices=GENDER,
                attrs={
                'class':'btn-check', # Bootstrap inside the forms.py
                
                }
            ),

             # smoker
            'smoker': forms.RadioSelect(
                choices=SMOKER,
                attrs={
                'class':'btn-check', # Bootstrap inside the forms.py
                
                }
            ),
        }