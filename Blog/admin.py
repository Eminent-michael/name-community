from django.contrib import admin


from .models import Blog, BlogComment

# Register your models here.

admin.site.register(BlogComment)

class BlogComment(admin.TabularInline):
    model = BlogComment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    inlines = [BlogComment]
    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)