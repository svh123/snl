from django.shortcuts import render
from django.http import *

# Create your views here.



def home_page(request):

    return render(request,'home.html')

def about_shop(request):

    return render(request,'about.html')

def mobile_contact(request):

    return render(request,'mobile.html')

def mail_contact(request):

    return render(request,'mail.html')

