from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_api(request):
    return HttpResponse("Blog_api")
