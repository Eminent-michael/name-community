from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model


from category.models import Category


User = get_user_model()

# Create your models here.


class CounselRoom(models.Model):
    host = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='counsel_user')
    info_public = models.BooleanField(default=False)
    topic = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique_for_date='created')
    description = models.TextField()
    participants = models.ManyToManyField(
        User, blank=True, related_name='participants')
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('counsel-room', args=[self.id, self.slug])


class Message(models.Model):
    room = models.ForeignKey(CounselRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:40]
