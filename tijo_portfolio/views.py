from django.shortcuts import render, redirect
from tijo_portfolio.models import Banner,Profile,Frontndskills,Backendskills, resume, experence, Projects, Contact, Project_video
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(arg):
    img=Banner.objects.first()
    pro=Profile.objects.first()
    fskl=Frontndskills.objects.all()
    bskl=Backendskills.objects.all()
    res=resume.objects.all()
    exp=experence.objects.first()
    pgt=Projects.objects.all()
    vdo=Project_video.objects.all()
    return render(arg, 'index.html', { 'img':img, 'pro':pro, 'fskl':fskl, 'bskl':bskl, 'res':res, 'exp':exp, 'pgt':pgt, 'vdo':vdo } )


