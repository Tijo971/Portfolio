from django.db import models

# Create your models here.
class Banner(models.Model):
    B_img=models.ImageField(upload_to="Banner", null=True, blank=True)


class Profile(models.Model):
    about=models.CharField(max_length=1000, null=True, blank=True)
    position=models.CharField(max_length=50, null=True, blank=True)
    Name=models.CharField(max_length=20, null=True, blank=True)
    Email=models.EmailField(max_length=30, null=True, blank=True)
    Dob=models.DateField(null=True, blank=True)
    P_num=models.IntegerField(null=True, blank=True)
    city=models.CharField(max_length=100, null=True, blank=True)
    degree=models.CharField(max_length=50, null=True, blank=True)
    web=models.CharField(max_length=50, null=True, blank=True)
    p_img=models.ImageField(upload_to='profile',null=True, blank=True)
    insta=models.CharField(max_length=50, null=True, blank=True)
    fcbk=models.CharField(max_length=50, null=True, blank=True)

class Frontndskills(models.Model):
    s_name=models.CharField(max_length=30, null=True, blank=True)
    s_value=models.IntegerField(null=True, blank=True)

class Backendskills(models.Model):
    s_name=models.CharField(max_length=30, null=True, blank=True)
    s_value=models.IntegerField(null=True, blank=True)

class resume(models.Model):
    Course=models.CharField(max_length=50, null=True, blank=True)
    collegename=models.CharField(max_length=50, null=True, blank=True)
    s_year=models.DateField(null=True, blank=True)
    e_year=models.DateField(null=True, blank=True)

class experence(models.Model):
    Company=models.CharField(max_length=60, null=True, blank=True)
    designation=models.CharField(max_length=50, null=True,blank=True)
    discriptions=models.CharField(max_length=1000, null=True, blank=True)
    cs_year=models.DateField(null=True, blank=True)
    ce_year=models.DateField(null=True, blank=True)

class Projects(models.Model):
    p_name=models.CharField(max_length=20, null=True, blank=True)
    p_dis=models.CharField(max_length=1000, null=True, blank=True)
    p_img=models.ImageField(upload_to='projects', null=True, blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=20, null=True, blank=True)
    email=models.EmailField()
    subject=models.CharField(max_length=500, null=True, blank=True)
    msg=models.CharField(max_length=2000, null=True, blank=True)

class Project_video(models.Model):
    name=models.CharField(max_length=30, null=True, blank=True)
    vdo=models.FileField(upload_to='p_videos/')
    
