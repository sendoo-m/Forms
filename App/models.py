from django.db import models

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

class Candidate(models.Model):
    firstname           = models.CharField(max_length=50)
    lastname            = models.CharField(max_length=50)
    job                 = models.CharField(max_length=10)
    age                 = models.CharField(max_length=3)
    phone               = models.CharField(max_length=12)
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
    
    # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname  =self.firstname.capitalize()        # to write all text reformat capitalize
        self.lastname   =self.lastname.capitalize()         # to write all text reformat capitalize

    def __str__(self):
        return self.firstname
