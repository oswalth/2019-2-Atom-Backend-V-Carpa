# Generated by Django 2.0 on 2019-11-06 07:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20191030_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-added_at',)},
        ),
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 7, 49, 25, 639921, tzinfo=utc)),
        ),
    ]