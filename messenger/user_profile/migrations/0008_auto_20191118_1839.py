# Generated by Django 2.2.5 on 2019-11-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20191118_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
