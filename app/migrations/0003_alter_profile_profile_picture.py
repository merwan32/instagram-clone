# Generated by Django 4.0.6 on 2022-08-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_profile_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default-user.png', upload_to='profilepics'),
        ),
    ]