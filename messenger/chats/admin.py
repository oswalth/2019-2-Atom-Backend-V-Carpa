from django.contrib import admin
from chats.models import Chat


# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('is_group_chat',)


admin.site.register(Chat, ChatAdmin)
