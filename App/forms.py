from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

# Every letters to LowerCase بديل ليها css تم كتابته بالاسفل ==============
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()
# Every letters to UpperCase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):
    # validations
    # First name 
    firstname       = forms.CharField(
        label       ='First Name',max_length=50, 
        min_length  =3 ,
        validators  =[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message     ="only letters is allowed !")], 
        widget      =forms.TextInput(attrs={
            'placeholder':'First name',
            'style': 'font-size: 13px; text-transform: capitalize'
            })
        )

    # last name
    lastname        = forms.CharField(
        label       ='Last Name',max_length=50, 
        min_length  =3 ,
        validators  =[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message     ="only letters is allowed !")], 
       widget      =forms.TextInput(attrs={
            'placeholder':'Last name',
            'style': 'font-size: 13px; text-transform: capitalize'
            })
        )

    # Job uppercase
    job           = Uppercase(
        label       ='Job Code', max_length=7, 
        min_length  =7,
        widget      =forms.TextInput(attrs={
            'placeholder':'Example FR-221',
                        'style': 'font-size: 13px; text-transform: uppercase'
            })
        )

    # e-mail lower case 
    email           = Lowercase(
        label       ='Email address', max_length=50, 
        min_length  =7,
        validators  =[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message     ="Put a valid email address !")], 
        widget      =forms.TextInput(attrs={
            'placeholder':'e-mail address',
            'style': 'font-size: 13px; text-transform: lowercase'
            })
        )

    #  Age Number only
    age           = forms.CharField(
        label       ='Your age', max_length=50, 
        min_length  =1,
        validators  =[RegexValidator(r'^[0-9]*$', 
        message     ="only number is allowd !")], 
        widget      =forms.TextInput(attrs={
            'placeholder':'Your age',
            'style': 'font-size: 13px'
            })
        )

    #  Phone Number only
    phone           = forms.CharField(
        label       ='phone', max_length=11, 
        min_length  =11,
        validators  =[RegexValidator(r'^[0-9]*$', 
        message     ="only number is allowd !")], 
        widget      =forms.TextInput(attrs={
            'placeholder':'Put a phone',
            'data-mask':'(00) 00000-0000',
            'style': 'font-size: 13px'
            })
        )
    
    # Experience
    experience     = forms.BooleanField(
        label = 'I Have experience', 
        required=False,
        )

    # Message
    message        = forms.CharField(
        label       ='about You', min_length=10, max_length=1000, required=False,
        widget      =forms.Textarea(attrs={
            'placeholder':'Talk a littel about you', 
            'rows':10,
            'style': 'font-size: 13px'
            })
    )

    # File Upload 
    file           = forms.FileField(
        required    = True,
        widget      = forms.ClearableFileInput(
            attrs   = {
                'style':'font-size: 13px'
            }
        )
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
            # 'Phone': forms.TextInput(
            #     attrs={
            #         'style': 'font-size: 13px',
            #         'placeholder':'Phone',
            #         # 'data-mask':'(00) 00000-0000',
            #     }
            # ),

            # salary
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                'class':'form-control', # Bootstrap inside the forms.py
                'style': 'font-size: 13px'
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

            # personality
            'personality': forms.Select(
                attrs={
                'style': 'font-size: 13px' # Bootstrap inside the forms.py
                
                }
            ),
        }

    # SUPER FUNCTION

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # ============ CONTROL PANAL ( Optiona method to control) ============|
        # 1- input requiered 
        # self.fields['experience'].required = True

        # 2- input Disabled 
        # self.fields['experience'].disabled = True

        # 3- input ReadOnly 
        # self.fields['email'].widget.attrs.update({'readonly':'readonly'})

        # 4- SELECT Optiona
        # self.fields["personality"].choices = [('','select a personality'),] + list(self.fields["personality"].choices)[1:]

        #  5- WIDGET inside/outside
        # self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder':'No Phone', 'data-mask': '(00) 00-000'})

        #  READONLY / DISAPER By Loop CONTROL
        # ReadOnly
        # readonly = ['firstname', 'lastname']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # ReadOnly
        # disabled = ['personality', 'age','salary','gender']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'