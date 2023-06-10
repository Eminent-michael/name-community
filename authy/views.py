from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms  import CustomCreateUserForm

# Create your views here.

def signUp(request):
    form = CustomCreateUserForm()
    if request.method == "POST":
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():
            form.save()        
    
    context = {"form":form}
    
    return render(request, "signup.html", context)
