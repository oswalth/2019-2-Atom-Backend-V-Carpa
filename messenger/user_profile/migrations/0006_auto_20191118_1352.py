# Generated by Django 2.2.5 on 2019-11-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20191113_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Ссылка на аватар'),
        ),
    ]
