# Generated by Django 2.0 on 2019-11-06 14:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_auto_20191106_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 14, 47, 19, 699546, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat', verbose_name='chat_id'),
        ),
    ]
