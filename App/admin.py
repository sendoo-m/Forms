from django.contrib import admin
from .models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html 
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# Admin Panel 
admin.site.site_header = 'LYS Form v 22.1.0 system Admin'
admin.site.index_title = "Table of Candidate"

class CandidateAdmin(ImportExportModelAdmin):  # ImportExportModelAdmin بديله عن   admin.ModelAdmin 
    radio_fields    = {"smoker": admin.HORIZONTAL} # to convert in admin panel to horizontal
    form            = CandidateForm
    exclude         = ['status'] # لإظهار الحالة والتحكم فيها
    list_display    = ['name','email','job','situation','created_at','status','_']
    search_fields   = ['firstname','lastname','email','situation']
    list_filter     = ['situation','firstname']
    list_per_page   = 10

    # # ReadOnly Section تم استبداله بالداله الخاصة بغلق الكل من على اليوزر والادمن  views.py array and form
    readonly_fields = ['firstname','lastname','job','email','phone','personality','salary','birth','gender','experience',
    'smoker','message','frameworks','languages','databases','libraries','mobile','others','file','image','status_course',
    'started_course','finished_course','course','institution','about_course','started_job','finished_job','about_job',
    'company','position','employed','remote','travel']# لجعل الحقول للقراءة فقط  

    # FILESET رائع بتنظيم صفحة الادمن
    fieldsets       = [
        # HR Operations
        ("HR OPERATIONS", {"fields": ['situation', 'company_note']}),
        # Personal
        ("PERSONAL", {"fields": ['firstname','lastname','job','email','phone',
        'personality','salary','birth','gender','experience','smoker','message','file','image',]}),
        # Skills
        ("SKILLS", {"fields": ['frameworks','languages','databases','libraries','mobile','others',]}),
        # Educational
        ("EDUCATIONAL", {"fields": ['status_course','started_course','finished_course','course',
        'institution','about_course',]}),
        # Professional
        ("PROFESSIONAL", {"fields": ['started_job','finished_job','about_job',
        'company','position']}),
        # Note
        ("NOTE", {"fields": ['employed','remote','travel']}),
    ]
    #  Function to Hide F-name and L-name (when clicking over the candidiate -Rows)
    def get_fields(self, request, obj = None):
        fields  =  super().get_fields(request, obj)
        if obj:
            fields.remove('firstname')
            fields.remove('lastname')
        return fields

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
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation)) # تستخدم مع اضافة  format_html
    status.allow_tages = True


admin.site.register(Candidate,CandidateAdmin)

# =================================================
