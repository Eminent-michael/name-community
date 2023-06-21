from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import CreateRoomForm
from .models import CounselRoom

# Create your views here.

def counselingHome(request):
    form = CreateRoomForm()
    
    template = loader.get_template("")
    
    context = {"form": form}
    return HttpResponse(template.render(context, request))