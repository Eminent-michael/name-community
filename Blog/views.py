from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateBlogForm

# Create your views here.

def creatBlog(request):
    forms = CreateBlogForm()
    context = {"forms":forms}
    return render(request, "Blog/creatPost.html", context)
