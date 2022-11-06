from django.contrib import admin
from .models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html


# Register your models here.
admin.site.site_header = 'LYS Form v 22.1.0 system Admin'

class CandidateAdmin(admin.ModelAdmin):
    radio_fields    = {"smoker": admin.HORIZONTAL} # to convert in admin panel to horizontal
    form            = CandidateForm
    exclude         = ['status'] # لإظهار الحالة والتحكم فيها
    # readonly_fields = ['firstname','lastname','email','job']  # لجعل الحقول للقراءة فقط  
    list_display    = ['firstname','lastname','email','job','situation','created_at','status','_']
    search_fields   = ['firstname','lastname','email','situation','age']
    list_filter     = ['situation','firstname','age']
    list_per_page   = 10

    # Function to change the Icon

    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    # Function to color text

    def status(self, obj):
        if obj.situation == 'Approved':
            color = '#28a745'
        elif obj.situation == 'Pending':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tages = True

admin.site.register(Candidate,CandidateAdmin)
