from django.contrib import admin
from .models import CounselRoom, Message

# Register your models here.

admin.site.register(Message)

class Message(admin.TabularInline):
    model = Message
    
class CounselRoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('topic',)}
    inlines = [Message]
    
admin.site.register(CounselRoom, CounselRoomAdmin)