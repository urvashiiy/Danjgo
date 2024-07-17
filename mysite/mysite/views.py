from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
   #return HttpResponse("Hello!! Lets start with django basic Home page")
   return render(request,'tutu.html')

def About(request):
    return HttpResponse("Hello!! Lets start with django basic Home page")

def Contact(request):
    return HttpResponse("Hello!! Lets start with django basic Conatct page")