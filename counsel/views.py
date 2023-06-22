from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .forms import CreateRoomForm
from .models import CounselRoom
from category.utils import categorySplit

# Create your views here.


def counselRoom(request, pk, slug):
    room = get_object_or_404(CounselRoom, id=pk, slug=slug)
    
    template = loader.get_template("Counsel/counselRoom.html")
    context = {}
    
    return HttpResponse(template.render(context, request))
    
    

def counselListPage(request):
    counsel_lists = CounselRoom.objects.all()
    
    template = loader.get_template("Counsel/counselListingPage.html")
    
    context = {"counsel_lists": counsel_lists}
    
    return HttpResponse(template.render(context, request))


def createCounselRoom(request):
    form = CreateRoomForm()
    user = request.user

    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data.get("topic")
            description = form.cleaned_data.get("description")
            categories = form.cleaned_data.get("categories")
            
            cat_obj = categorySplit(request, categories)

            created = CounselRoom.objects.create(topic=topic, description=description)
            created.categories.set(cat_obj)
            created.save()
            
    template = loader.get_template("Counsel/createRoom.html")

    context = {"form": form}
    return HttpResponse(template.render(context, request))
