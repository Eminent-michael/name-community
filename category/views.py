from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def categories(request):
    return HttpResponse("This is categories page")