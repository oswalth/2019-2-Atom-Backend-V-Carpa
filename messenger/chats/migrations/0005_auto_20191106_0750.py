# Generated by Django 2.0 on 2019-11-06 07:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20191106_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 7, 50, 17, 946981, tzinfo=utc)),
        ),
    ]