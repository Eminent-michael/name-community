# Generated by Django 4.1.7 on 2023-04-01 15:53

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_alter_profile_country_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='./user.png', null=True, upload_to=authy.models.user_directory_path),
        ),
    ]
