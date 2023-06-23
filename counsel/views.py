from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Models imports

from .forms import CreateRoomForm, MessageForm
from .models import CounselRoom, Message
from category.utils import categorySplit

# Create your views here.


def counselRoomPage(request, pk, slug):
    user = request.user.id
    room = get_object_or_404(CounselRoom, id=pk, slug=slug)
    messages = Message.objects.filter(room_id=pk).all()
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("body")
            room_id = request.POST.get("room_id")
            
            new_message = Message.objects.create(user_id=user, body=message, room_id =room_id)
            
            room.participants.add(user)
            
            new_message.save()
    form = MessageForm()
    template = loader.get_template("Counsel/counselRoom.html")
    context = {"room": room, "messages":messages, "form":form}
    
    return HttpResponse(template.render(context, request))
    
    

def counselListPage(request):
    counsel_lists = CounselRoom.objects.all()
    
    template = loader.get_template("Counsel/counselListingPage.html")
    
    context = {"counsel_lists": counsel_lists}
    
    return HttpResponse(template.render(context, request))


def createCounselRoom(request):
    form = CreateRoomForm()
    user = request.user.id

    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data.get("topic")
            description = form.cleaned_data.get("description")
            categories = form.cleaned_data.get("categories")
            
            cat_obj = categorySplit(request, categories)

            created = CounselRoom.objects.create(host_id=user, topic=topic, description=description)
            created.categories.set(cat_obj)
            created.save()
        else:
            form = CreateRoomForm()
            
    template = loader.get_template("Counsel/createRoom.html")

    context = {"form": form}
    return HttpResponse(template.render(context, request))
