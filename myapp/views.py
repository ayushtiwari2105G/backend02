from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePage(request):
    return HttpResponse("Welcome to my website")
def myname(request):
    return HttpResponse("My name is John Doe")

def myage(request):
    return HttpResponse("I am 25 years old")

def myaddress(request):
    return HttpResponse("I live in New York City")

def myhobbies(request):
    return HttpResponse("I enjoy playing soccer and reading")
