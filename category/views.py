from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Import Models
from .models import Category
from Blog.models import Blog

# Create your views here.


def categories(request, title):
    categories = Category.objects.filter(title__iexact=title).all()
    cat_list = []

    for category in categories:
        cat_list.append(category)

    results = Blog.objects.filter(
        categories__in=cat_list).all().order_by("-publish")

    template = loader.get_template("Blog/categoryPage.html")
    context = {"title": title, "results": results}

    return HttpResponse(template.render(context, request))
