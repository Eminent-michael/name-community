from django import forms
from .models import Blog

# Create Blog form


class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={}))
    body = forms.CharField(widget=forms.Textarea(attrs={}))
    categories = forms.CharField(widget=forms.TextInput(attrs={}))
    minute_read = forms.IntegerField(widget=forms.TextInput(attrs={}))
    status = forms.ChoiceField(choices=Blog.STATUS_CHOICE)

    class Meta:
        model = Blog
        fields = ("title", "categories", "body", "minute_read", "status")
