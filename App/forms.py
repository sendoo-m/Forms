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
    
    experience     = forms.BooleanField(label = 'I Have experience', required=False,
       
    )

    message        = forms.CharField(
        label       ='about You', min_length=10, max_length=1000, required=False,
        widget      =forms.Textarea(attrs={'placeholder':'Talk a littel about you', 'rows':10})
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

    # SUPER FUNCTION

    # def __init__(self, *args, **kwargs):
    #     super(CandidateForm, self).__init__(*args, **kwargs)

        # ============ CONTROL PANAL ( Optiona method to control) ============|
        # input requiered 
        # self.fields['experience'].required = True

        # input Disabled 
        # self.fields['experience'].disabled = True
        # ============ SELECT Optiona  ============|
        # self.fields["personality"].choices = [('','select a personality'),] + list(self.fields["personality"].choices)[1:]

        # ============ WIDGET CONTROL  ============|
        # self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder':'No Phone', 'data-mask': '(00) 00-000'})

        # ============ READONLY / DISAPER By Loop CONTROL  ============|
        # ReadOnly
        # readonly = ['firstname', 'lastname']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # ReadOnly
        # disabled = ['personality', 'age','salary','gender']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'