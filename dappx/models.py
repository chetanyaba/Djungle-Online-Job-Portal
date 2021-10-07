

# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
class Shortlist(models.Model):
    nameofemp = models.CharField(max_length=100)

    name_of_company = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    stipend=models.IntegerField(default=None)

class postajob(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    desc = models.TextField()
    pay = models.IntegerField(default=0)
    JOB_TYPE = (
        ('1', "Full time"),
        ('2', "Part time"),
        ('3', "Internship"),
        ('4', "freelance"),
        ('5', "temporary")
    )

    type = models.CharField(choices=JOB_TYPE, max_length=20)
    field = models.CharField( max_length=20)

    def __str__(self):
        return self.job_title






class candidate_info(models.Model):
    first_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,default=None)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    location=models.CharField(max_length=100)
    college_name=models.CharField(max_length=100)
    JOB_TYPE = (
        ('1', "Full time"),
        ('2', "Part time"),
        ('3', "Internship"),
        ('4', "freelance"),
        ('5', "temporary")
    )
    type=models.CharField(choices=JOB_TYPE,max_length=20,default='3')
    fieldofinterest=models.CharField(max_length=100,default=None)
    cv=models.TextField()
    image=models.ImageField(upload_to='profile_pics',default='media/profile_pic/sam.jpeg')


    def __str__(self):
        return self.first_name




class Blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    desc=models.TextField()
    like=models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Message(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    mess=models.TextField()
