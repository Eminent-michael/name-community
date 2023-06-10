# Generated by Django 4.1.7 on 2023-04-01 16:15

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0008_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='./user.png', null=True, upload_to=authy.models.user_directory_path, verbose_name='picture'),
        ),
    ]
