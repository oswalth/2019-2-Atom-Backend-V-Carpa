# Generated by Django 2.2.5 on 2019-12-02 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attachment', '0002_attachment_chat'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='message.Message', verbose_name='Сообщение вложения'),
        ),
    ]