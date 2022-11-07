from email.policy import default
from random import choices
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
SITUATION   = (
    ('pending','pending'),
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
class Candidate(models.Model):
    firstname           = models.CharField(max_length=50)
    lastname            = models.CharField(max_length=50)
    job                 = models.CharField(max_length=10)
    age                 = models.CharField(max_length=3)
    phone               = models.CharField(max_length=15)
    personality         = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary              = models.CharField(max_length=50)
    gender              = models.CharField(max_length=50)
    experience          = models.BooleanField(null=True)
    smoker              = models.CharField(max_length=10, choices=SMOKER, default='No')
    email               = models.EmailField(max_length=50)
    message             = models.TextField()
    file                = models.FileField()
    created_at          = models.DateTimeField(auto_now_add=True)
    situation           = models.CharField(max_length=50, null=True, choices=SITUATION, default='pending')
    # Multiple Check 
    frameworks          = MultiSelectField(choices=FRAMEWORKS, default="")
    languages           = MultiSelectField(choices=LANGUAGES, default="")
    databases           = MultiSelectField(choices=DATABASES, default="")
    libraries           = MultiSelectField(choices=LIBRARIES, default="")
    mobile              = MultiSelectField(choices=MOBILE, default="")
    others              = MultiSelectField(choices=OTHERS, default="")
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