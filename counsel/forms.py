from django import forms

from .models import CounselRoom, Message


class CreateRoomForm(forms.ModelForm):
    topic = forms.CharField(widget=forms.TextInput(attrs={}))
    description = forms.CharField(widget=forms.Textarea(attrs={}))
    categories = forms.CharField(widget=forms.TextInput(attrs={}))
    
    class Meta:
        model = CounselRoom
        fields = ["topic", "description", "categories"]
        
        
class MessageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Write your message here"}))
    
    class Meta:
        model = Message
        fields = ["body"]