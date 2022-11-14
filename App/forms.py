import email
from django import forms
from .models import Candidate
from django.core.validators import RegexValidator # لعمل صلاحيات خاصة على الحقول 
from django.core.exceptions import ValidationError # مستخدم في داله عدم تكرار المدخلات

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
        error_messages={'required':'انت اهبل ياض الاسم غلط'}, 
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
        label       ='Job Code', max_length=6, 
        min_length  =6,
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
    # age           = forms.CharField(
    #     label       ='Your age', max_length=50, 
    #     min_length  =1,
    #     validators  =[RegexValidator(r'^[0-9]*$', 
    #     message     ="only number is allowd !")], 
    #     widget      =forms.TextInput(attrs={
    #         'placeholder':'Your age',
    #         'style': 'font-size: 13px'
    #         })
    #     )

    #  Phone Number only
    phone           = forms.CharField(
        label       ='phone', max_length=11, 
        min_length  =11,
        validators  =[RegexValidator(r'^[0-9]*$', 
        message     ="only number is allowd !")], # الرسالة عند كتابة رقم غير مطابق للشرط
        # error_messages={'required':'الرقم غلط يا معلم'}, ## عدم وجود رقم تم كتابته 
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
        label       ='about You', min_length=10, max_length=1000,
        widget      =forms.Textarea(attrs={
            'placeholder':'Talk a littel about you', 
            'rows':6,
            'style': 'font-size: 13px'
            })
    )

    # File Upload 
    file           = forms.FileField(
        label       = 'Resume',
        widget      = forms.ClearableFileInput(
            attrs   = {
                'style':'font-size: 13px',
                'accept':'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            }
        )
    )

    # Image Upload 
    image           = forms.FileField(
        label       = 'Photo',
        widget      = forms.ClearableFileInput(
            attrs   = {
                'style':'font-size: 13px',
                'accept':'image/png, image/jpeg',
            }
        )
    )

    # Institution
    institution     = forms.CharField(
        label       = 'institution', 
        max_length  = 50, 
        min_length  = 3,
        # error_messages={'required':'الرقم غلط يا معلم'}, ## عدم وجود رقم تم كتابته 
        widget      = forms.TextInput(
            attrs   = {
            'style':'font-size: 13px',
            'placeholder':'Institution name',
    })
    )

    # College course
    course     = forms.CharField(
        label       = 'course', 
        max_length  = 50, 
        min_length  = 3,
        widget      = forms.TextInput(
            attrs   = {
            'style':'font-size: 13px',
            'placeholder':'Your college course',
    })
    )

    # Company
    company         = forms.CharField(
        label       = 'Last company', 
        max_length  = 50, 
        min_length  = 3,
        widget      = forms.TextInput(
            attrs   = {
            'style':'font-size: 13px',
            'placeholder':'Company name',
    })
    )

    # position
    position         = forms.CharField(
        max_length  = 50, 
        min_length  = 3,
        widget      = forms.TextInput(
            attrs   = {
            'style':'font-size: 13px',
            'placeholder':'Your occupation',
    })
    )

    # About college Course
    about_course    = forms.CharField(
        label       ='about Your college course', min_length=10, max_length=1000,
        widget      =forms.Textarea(attrs={
            'placeholder':'Tell us about college course ...', 
            'rows':7,
            'style': 'font-size: 13px'
            })
    )

    # About Job
    about_job       = forms.CharField(
        label       ='about Your job', min_length=10, max_length=1000,
        widget      =forms.Textarea(attrs={
            'placeholder':'Tell us alittle about what you did at the company job ...', 
            'rows':7,
            'style': 'font-size: 13px'
            })
    )

    employed        = forms.BooleanField(label='I am employed', required=False)
    remote          = forms.BooleanField(label='I agree to work remotly', required=False)
    travel        = forms.BooleanField(label="I'm available for travel ", required=False)


    class Meta:
        model       = Candidate
        # fields      = '__all__'
        # fields      = ['firstname','lastname','age','email','message']
        exclude     = ['situation','created-at']
        labels      = {
            'gender':'Your Gender',
            'smoker': 'Do you smoker?',
            'started_course':'Started',
            'finished_course':'Finished',
            'started_job':'Started',
            'finished_job':'Finished',
        }

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
            # Birthday
            'birth': forms.DateInput(
                attrs={
                'style': 'font-size: 13px; cursor: pointer',
                'type': 'date',
                'onkeydown':'return false', # Block typing inside the input
                'min':'1950-01-01',
                'max':'2030-01-01',
                }
            ),

            # Start course
            'started_course': forms.DateInput(
                attrs={
                'style': 'font-size: 13px; cursor: pointer',
                'type': 'date',
                'onkeydown':'return false', # Block typing inside the input
                'min':'1950-01-01',
                'max':'2030-01-01',
                }
            ),

            # finish course
            'finished_course': forms.DateInput(
                attrs={
                'style': 'font-size: 13px; cursor: pointer',
                'type': 'date',
                'onkeydown':'return false', # Block typing inside the input
                'min':'1950-01-01',
                'max':'2030-01-01',
                }
            ),

            # Start job
            'started_job': forms.DateInput(
                attrs={
                'style': 'font-size: 13px; cursor: pointer',
                'type': 'date',
                'onkeydown':'return false', # Block typing inside the input
                'min':'1950-01-01',
                'max':'2030-01-01',
                }
            ),

            # finish job
            'finished_job': forms.DateInput(
                attrs={
                'style': 'font-size: 13px; cursor: pointer',
                'type': 'date',
                'onkeydown':'return false', # Block typing inside the input
                'min':'1950-01-01',
                'max':'2030-01-01',
                }
            ),

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
# دا بداية الدالة لكل الاوامر بالاسفل
def __init__(self, *args, **kwargs):
    super(CandidateForm, self).__init__(*args, **kwargs)

        # ============ CONTROL PANAL ( Optiona method to control) ============|
        # 1- input requiered # مطلوب الكتابة ولا يمكن الاستكمال بدونه
        # self.fields['experience'].required = True

        # 2- input Disabled # عدم السماح بالتسجيل والكتابة
        # self.fields['experience'].disabled = True

        # 3- input ReadOnly # لجعل الحقل للقراءة فقط
        # self.fields['email'].widget.attrs.update({'readonly':'readonly'})

        # 4- SELECT Optiona # يقوم بتقليل عدد الاختيارات عند استخدام 0 يظهر الكل عند استخدام 6 يقوم بالغاء الكل وعدم اظهارهم
        # self.fields["personality"].choices = [('','select a personality'),] + list(self.fields["personality"].choices)[1:]

        #  5- WIDGET inside/outside
        # self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder':'No Phone', 'data-mask': '(00) 00-00'})


        #  READONLY / DISAPER By Loop CONTROL   ======== Method 2 ========
        # ReadOnly
        # readonly = ['firstname', 'lastname']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # Disabled                              ======== Method 2 ========
        # disabled = ['personality', 'age','salary','gender']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'

        # Error Message                         ======== Method 2 ========
        # تستخدم لوضع رساله خطاء لكل الحقول في حالة عدم وضع اى بيانات
        # error_message  = ['firstname','lastname','phone','age','email','message','smoker','gender']
        # for field in error_message:
        #     self.fields[field].error_messages.update({'required': 'Mohamed Gamal Sendoo'})

    # ================= End // Supper funcations ================= #

    # function to prevent Duplicated Enteries

    # method (1) Loop For

# dont register duplecate email
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         for obj in Candidate.objects.all():
#             if obj.email == email:
#                 raise forms.ValidationError('Denied ! ' + email + ' is already Registered')
#         return email

# # dont register duplecate firstname
#     def clean_firstname(self):
#             firstname = self.cleaned_data.get('firstname')
#             for obj in Candidate.objects.all():
#                 if obj.firstname == firstname:
#                     raise forms.ValidationError('Denied ! ' + firstname + ' is already Registered')
#             return firstname

# # dont register duplecate firstname
#     def clean_firstname(self):
#             firstname = self.cleaned_data.get('firstname')
#             for obj in Candidate.objects.all():
#                 if obj.firstname == firstname:
#                     raise forms.ValidationError('Denied ! ' + firstname + ' is already Registered')
#             return firstname

# # dont register duplecate phone
#     def clean_phone(self):
#             phone = self.cleaned_data.get('phone')
#             for obj in Candidate.objects.all():
#                 if obj.phone == phone:
#                     raise forms.ValidationError('Denied ! ' + phone + ' is already Registered')
#             return phone
    
    # Method (2) If
#######============ عدم تكرار في الحقول ============#########
# # # dont register duplecate phone
#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#         if Candidate.objects.filter(phone = phone).exists():
#             raise forms.ValidationError('Denied ! {} is already Registered'.format(phone))
#         return phone

# # # dont register duplecate firstname
#     def clean_firstname(self):
#         firstname = self.cleaned_data.get('firstname')
#         if Candidate.objects.filter(firstname = firstname).exists():
#             raise forms.ValidationError('Denied ! {} is already Registered'.format(firstname))
#         return firstname

# # # dont register duplecate lastname
#     def clean_lastname(self):
#         lastname = self.cleaned_data.get('lastname')
#         if Candidate.objects.filter(lastname = lastname).exists():
#             raise forms.ValidationError('Denied ! {} is already Registered'.format(lastname))
#         return lastname

# # # dont register duplecate email
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if Candidate.objects.filter(email = email).exists():
#             raise forms.ValidationError('Denied ! {} is already Registered'.format(email))
#         return email
#######============ نهاية عدم تكرار في الحقول ============#########

# ===================== Control Panel  ===================== #
# رسالة تطلع لو مكتبش حاجة اصلا  دا باقي الجزء بالاعلي 
    self.fields['firstname'].error_messages.update({
        'required' : 'انت هتشتغلني حط اسم يا معلم'
    })

    self.fields['phone'].error_messages.update({
        'required' : 'مش واجب تسجل برقم ولا دي صفحة من الشارع يعني'
    })