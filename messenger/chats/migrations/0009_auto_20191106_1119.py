# Generated by Django 2.0 on 2019-11-06 11:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_auto_20191106_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 11, 19, 39, 440520, tzinfo=utc)),
        ),
    ]
