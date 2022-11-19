from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Candidate
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required # login required to access private pages.
from django.views.decorators.cache import cache_control # Destory the section after log out.
from django.core.paginator import Paginator
from django.db.models import Q # for search
# Concatenated F-name and L-name
from django.db.models.functions import Concat # Concatenated
from django.db.models import Value as P #(P=Plus)


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
    # Filter (individual)
    # if request.method == 'POST':
    #     job         = request.POST.get('job')
    #     filter      = Candidate.objects.filter(job=job)
    #     context     = {
    #         "candidates" : filter
    #     }
    #     return render(request, 'backend.html', context)

    # Global filter
    if request.method == 'POST':
        job         = request.POST.get('job')
        gender      = request.POST.get('gender')
        filter      = Candidate.objects.filter(Q(job=job) |Q(gender=gender))
        context     = {
            "candidates" : filter
        }
        return render(request, 'backend.html', context)

    # Global Search
    elif 'q' in request.GET:
        q                   = request.GET['q']
        all_candidate_list  = Candidate.objects.annotate(
            name            = Concat('firstname', P(' '), 'lastname')).\
            filter(Q(name__icontains=q) | Q(firstname__icontains=q) | Q(lastname__icontains=q) |
            Q(email__icontains=q) | Q(email__icontains=q) | Q(phone__icontains=q)) # very important space in P('Space') and P capital
    else:
        all_candidate_list  = Candidate.objects.all().order_by('-created_at')
        # Pagination
    paginator           = Paginator(all_candidate_list, 3)
    page                = request.GET.get('page')
    all_candidate       = paginator.get_page(page)

    context     = {
        'candidates':all_candidate
    } 
    return render(request, 'backend.html', context)

# Access candidate individually
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request, id):
    candidate        = Candidate.objects.get(pk = id)
    return render(request, 'candidate.html', {'candidate': candidate})
