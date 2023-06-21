from django import forms

from .models import CounselRoom


class CreateRoomForm(forms.ModelForm):
    topic = forms.CharField(widget=forms.TextInput(attrs={}))
    description = forms.CharField(widget=forms.Textarea(attrs={}))
    
    class Meta:
        model = CounselRoom
        fields = ["topic", "description", "categories"]