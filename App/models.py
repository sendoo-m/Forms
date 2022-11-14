from email.policy import default
from random import choices
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
SITUATION   = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved')
)
PERSONALITY   = (
    ('','select a personality'),
    ('I am outgoing','I am outgoing'),
    ('I am sociable','I am sociable'),
    ('I am antisocial','I am antisocial'),
    ('I am disceet','I am disceet'),
    ('I am serious','I am serious')
)
# GENDER   = (
#     ('Male','Male'),
#     ('Female','Female')
# )

SMOKER   = (
    ('1','Yes'),
    ('2','No')
)

# Multiple Check
FRAMEWORKS = (
    ('Laravel','Laravel'),
    ('Angular','Angular'),
    ('Django','Django'),
    ('Flask','Flask'),
    ('Vue','Vue'),
    ('Others','Others')
)

LANGUAGES = (
    ('Python','Python'),
    ('Javascript','Javascript'),
    ('Java','Java'),
    ('C++','C++'),
    ('Ruby','Ruby'),
    ('Others','Others')
)

DATABASES = (
    ('MySql','MySql'),
    ('Postgree','Postgree'),
    ('MongoDB','MongoDB'),
    ('SqLite3','SqLite3'),
    ('Oracle','Oracle'),
    ('Others','Others')
)

LIBRARIES = (
    ('Ajax','Ajax'),
    ('Jquery','Jquery'),
    ('React.js','React.js'),
    ('Chart.js','Chart.js'),
    ('Gsap','Gsap'),
    ('Others','Others')
)

MOBILE = (
    ('React native','React native'),
    ('Kivy','Kivy'),
    ('Flutter','Flutter'),
    ('Ionic','Ionic'),
    ('Xamarim','Xamarim'),
    ('Others','Others')
)

OTHERS = (
    ('UML','UML'),
    ('SQL','SQL'),
    ('Docker','Docker'),
    ('GIT','GIT'),
    ('GraphQL','GraphQL'),
    ('Others','Others')
)

STATUS_COURSE = (
    ('','Select your status course'),
    ("i' am studying","i' am studying"),
    ('I took a break','I took a break'),
    ('Complated','Complated')
)
class Candidate(models.Model):
    # Personal Card (1)
    firstname           = models.CharField(max_length=50)
    lastname            = models.CharField(max_length=50)
    job                 = models.CharField(max_length=10)
    # age                 = models.CharField(max_length=3)
    birth               = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Birthday')
    phone               = models.CharField(max_length=15)
    personality         = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary              = models.CharField(max_length=50)
    gender              = models.CharField(max_length=50)
    experience          = models.BooleanField(null=True)
    smoker              = models.CharField(max_length=10, choices=SMOKER, default='No')
    email               = models.EmailField(max_length=50)
    message             = models.TextField()
    file                = models.FileField(upload_to='resume', blank=True, verbose_name='Resume')
    image               = models.ImageField(upload_to='photo', blank=True, verbose_name='Photo')
    created_at          = models.DateTimeField(auto_now_add=True)
    situation           = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
    company_note        = models.TextField(blank=True)
    # Skill Card(2)  
    frameworks          = MultiSelectField(choices=FRAMEWORKS, default="")
    languages           = MultiSelectField(choices=LANGUAGES, default="")
    databases           = MultiSelectField(choices=DATABASES, default="")
    libraries           = MultiSelectField(choices=LIBRARIES, default="")
    mobile              = MultiSelectField(choices=MOBILE, default="")
    others              = MultiSelectField(choices=OTHERS, default="")
    # Educational Card(3)
    institution         = models.CharField(max_length=50)
    course              = models.CharField(max_length=50)
    started_course      = models.DateField(auto_now=False, auto_now_add=False)
    finished_course     = models.DateField(auto_now=False, auto_now_add=False)
    about_course        = models.TextField()
    status_course       = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)

    # Professional Card(4) 

    company             = models.CharField(max_length=50)
    position            = models.CharField(max_length=50)
    started_job         = models.DateField(auto_now=False, auto_now_add=False)
    finished_job        = models.DateField(auto_now=False, auto_now_add=False)
    about_job           = models.TextField()
    employed            = models.BooleanField(null=True, verbose_name='I am employed')
    remote              = models.BooleanField(null=True, verbose_name='I agree to work remotly')
    travel              = models.BooleanField(null=True, verbose_name="I'm availbale for travel")

    def __str__(self):
        return self.firstname

    # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname  =self.firstname.capitalize()        # to write all text reformat capitalize
        self.lastname   =self.lastname.capitalize()         # to write all text reformat capitalize

    # Concatenate F-name and L-name (Admin Table)
    # جمع عمودين بالادمن مثل الاسم الاول والاخير ثم يتم ازالة الاسم الاول والاخير من ملف الادمن list

    def name(obj):
        return "%s %s" %(obj.firstname, obj.lastname)

     # Concatenate F-name and L-name when click over name in admin لإظهار الاسم بالكامل
    def __str__(self):
        return self.firstname + ' ' + self.lastname