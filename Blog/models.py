from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField

from category.models import Category

# Create your models here

def user_directory_path(instance, filename):
    return 'user_{0}/name_community-{1}'.format(instance.author, filename)


User = get_user_model()


class Blog(models.Model):
    STATUS_CHOICE = (
        ("draft", "Draft"),
        ("publish", 'Publish')
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    categories = models.ManyToManyField(Category, blank=True)
    # body = models.TextField()
    body = RichTextField(config_name= 'default', null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=12, choices=STATUS_CHOICE, default='draft')
    minute_read = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog-details', args=[self.slug, self.publish.month])
    
    
class BlogComment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)