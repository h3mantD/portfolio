from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User 

DEPARTMENT_CHOICES = [
    ('none', 'Select Department'),
    ('comp', 'Computer'),
    ('it', 'Information Technology'),
    ('mech', 'Mechanical'),
    ('civil', 'Civil'),
    ('etc', 'E and TC'),
    ('elc', 'Electrical')
]
CLASS_CHOICES = [
    ('none', 'Select Class'),
    ('fe', 'First Year'),
    ('se', 'Second Year'),
    ('te', 'Third Year'),
    ('be', 'Final Year'),
]


class userdata(models.Model):
    #studid = models.ForeignKey(User, on_delete=models.CASCADE, default='null')
    studid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(
        max_length =10,
        choices = DEPARTMENT_CHOICES,
        default = 'none',
    )
    classis = models.CharField(
        max_length = 5,
        choices = CLASS_CHOICES,
        default = 'none',
    )
    roll_no = models.PositiveIntegerField()
    tenth_marks = models.PositiveIntegerField()
    twelth_marks = models.PositiveIntegerField()
    degree_marks = models.PositiveIntegerField()
    live_back = models.PositiveIntegerField()
    add_info = models.CharField(max_length = 1000, blank=True)
    resume = models.FileField(blank=True)

    def get_absolute_url(self):
        return reverse('studdata', kwargs={'id':self.studid})
    
    def __str__(self):
        return str(self.studid)

class companyData(models.Model):
    cname = models.CharField(unique=True, max_length=100)
    tenth_marks = models.PositiveIntegerField()
    twelth_marks = models.PositiveIntegerField()
    degree_marks = models.PositiveIntegerField()
    live_back = models.PositiveIntegerField()
    selected_stud = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cname

class selected(models.Model):
    cname = models.CharField(max_length=100)
    studid = models.PositiveIntegerField()
    s_username = models.CharField(max_length=100)

    def __str__(self):
        return self.cname




