from django import forms
from .models import Blog, BlogComment
from ckeditor.widgets import CKEditorWidget
# Create Blog form


class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={}))
    body = forms.CharField(widget=CKEditorWidget())
    categories = forms.CharField(widget=forms.TextInput(attrs={}))
    minute_read = forms.IntegerField(widget=forms.NumberInput(attrs={}))
    status = forms.ChoiceField(choices=Blog.STATUS_CHOICE)

    class Meta:
        model = Blog
        fields = ("title", "categories", "body", "minute_read", "status")


class BlogCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs=""))
    
    class Meta:
        model = BlogComment
        fields = ("body",)