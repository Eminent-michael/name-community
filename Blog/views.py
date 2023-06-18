from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateBlogForm
from .models import Blog
from category.models import Category

# Create your views here.


def creatBlog(request):
    user = request.user
    print(user)
    cat_objs = []
    form = CreateBlogForm()
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        print(request)
        if form.is_valid():
            print("it is valid")
            title = form.cleaned_data.get("title")
            body = form.cleaned_data.get("body")
            categories = form.cleaned_data.get("categories")
            minute_read = form.cleaned_data.get("minute_read")
            status = form.cleaned_data.get("status")
            # print("status " + status)

            # Categories separations
            cat_list = list(categories.replace(" ", "").split(","))

            for cat in cat_list:
                c, cat = Category.objects.get_or_create(title=cat)
                cat_objs.append(c)

            created = Blog.objects.create(
                author_id=user, body=body, minute_read=minute_read, status=status)

            created.categories.set(cat_objs)
            form.save()

        else:
            print("Form contents not valid......")

    context = {"form": form}
    return render(request, "Blog/creatPost.html", context)
