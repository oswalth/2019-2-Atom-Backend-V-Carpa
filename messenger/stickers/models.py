from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128, null=True)
    nick = models.CharField(max_length=32)


class Chat(models.Model):
    participant = models.ManyToManyField(User)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='host')
