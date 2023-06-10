from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def counselingHome(request):
    return HttpResponse("Counseling Page")