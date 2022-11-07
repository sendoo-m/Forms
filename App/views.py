from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Candidate
from django.core.exceptions import ValidationError

def home(request):
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
            return render(request, "home.html", context)
    else:
        form    = CandidateForm()
        context = {
                "form":form
            }
        return render(request, "home.html", context)

#######============ عدم تكرار في الحقول ============#########
# # dont register duplecate phone
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Candidate.objects.filter(phone = phone).exists():
            raise forms.ValidationError('Denied ! {} is already Registered'.format(phone))
        return phone

# # dont register duplecate firstname
    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if Candidate.objects.filter(firstname = firstname).exists():
            raise forms.ValidationError('Denied ! {} is already Registered'.format(firstname))
        return firstname

# # dont register duplecate lastname
    def clean_lastname(self):
        lastname = self.cleaned_data.get('lastname')
        if Candidate.objects.filter(lastname = lastname).exists():
            raise forms.ValidationError('Denied ! {} is already Registered'.format(lastname))
        return lastname

# # dont register duplecate email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email = email).exists():
            raise forms.ValidationError('Denied ! {} is already Registered'.format(email))
        return email
#######============ نهاية عدم تكرار في الحقول ============#########
