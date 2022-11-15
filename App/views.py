from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Candidate
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required # login required to access private pages.
from django.views.decorators.cache import cache_control # Destory the section after log out.


# ======================== FRONTEND ======================== |

# HOME 
def home(request):
    return render(request, 'home.html')

# CANDIDATE REGISTER
def register(request):
    if request.method == "POST":

        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Sent successfully !")
            return HttpResponseRedirect('/')
        else:
            context = {
                "form":form
            }
            return render(request, "register.html", context)
    else:
        form    = CandidateForm()
        context = {
                "form":form
            }
        return render(request, "register.html", context)

# #######============ عدم تكرار في الحقول ============#########
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


# ======================== BACKEND ======================== |

# HR - Home Page (backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    context     = {
        'data_read':Candidate.objects.all()
    } 
    return render(request, 'backend.html', context)

# Access candidate individually
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request, id):
    data        = Candidate.objects.get(pk = id)
    form        = CandidateForm(instance = data)
    array       = ['firstname','lastname','job','email','phone','personality','salary','birth','gender','experience',
                        'smoker','message','frameworks','languages','databases','libraries','mobile','others','file','image','status_course',
                        'started_course','finished_course','course','institution','about_course','started_job','finished_job','about_job',
                        'company','position','employed','remote','travel']
    for field in array:
        form.fields[field].disabled = True
        form.fields['file'].widget.attrs.update({'style': 'display: none'})
        form.fields['image'].widget.attrs.update({'style': 'display: none'})
    context     = {
        'form':form
    }
    return render(request, 'candidate.html', context)
