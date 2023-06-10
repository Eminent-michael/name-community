from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import os
from django.conf import settings
from PIL import Image

from django_countries.fields import CountryField


# Models import

from Blog.models import Blog

# Create your models here.


def user_directory_path(instance, filename):
    profile_pic_name = 'user_{0}/profile.jpg'.format(
        instance.user.id, filename)

    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_pic_name


User_ = get_user_model()


class Profile(models.Model):

    Gender = (
        ('none', 'None'),
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(User_, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=20)
    profile_info = models.TextField(max_length=259,  null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    country = CountryField(null=True)
    gender = models.CharField(max_length=10, default='none', choices=Gender)
    email = models.EmailField(null=True)
    picture = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, verbose_name='picture', default='./user.png'
        )
    favorite = models.ManyToManyField(Blog, blank=True)
    created = models.DateField(auto_now_add=True)

    @property
    def imageurl(self):
        try:
            url = self.picture.url
        except:
            url = '/media/user.png'

        return url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 300, 300

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,
                               username=instance.username,
                               email=instance.email
                               )
        print("Profile created!!")


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # ? Know how this works
    print(instance, "---This what is going on with save_user_profile.")


post_save.connect(create_user_profile, sender=User_)
post_save.connect(save_user_profile, sender=User)
