from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .forms import CreateBlogForm, BlogCommentForm
from .models import Blog, BlogComment
from category.models import Category
from category.utils import categorySplit

# Create your views here.


def blogDetail(request, pk, post):
    blog = get_object_or_404(Blog, id=pk, slug=post)
    user = request.user.id

    comments = BlogComment.objects.filter(blog_id=pk).all()

    comment_form = BlogCommentForm()

    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            blog_id = request.POST.get("blog_id")
            comment_body = form.cleaned_data.get("body")

            new_comment = BlogComment.objects.create(
                user_id=user, blog_id_id=blog_id, body=comment_body)
            new_comment.save()

    template = loader.get_template("Blog/blogDetail.html")
    context = {"blog": blog, "comment_form": comment_form, "comments": comments}

    return HttpResponse(template.render(context, request))


def blogHomePage(request):
    blogs = Blog.objects.all().filter(status="draft")

    context = {"blogs": blogs}
    return render(request, "Blog/blogHomePage.html", context)


def createBlog(request):
    user = request.user.id
    print("user")
    form = CreateBlogForm()
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            print("it is valid")
            title = form.cleaned_data.get("title")
            body = form.cleaned_data.get("body")
            categories = form.cleaned_data.get("categories")
            minute_read = form.cleaned_data.get("minute_read")
            status = form.cleaned_data.get("status")

            cat_objs = categorySplit(categories)

            created = Blog.objects.create(
                author_id=user, body=body, minute_read=minute_read, status=status, title=title)

            created.categories.set(cat_objs)
            created.save()

    context = {"form": form}
    return render(request, "Blog/creatPost.html", context)
