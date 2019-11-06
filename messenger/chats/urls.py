from chats.views import chat_list, create_chat, list_chats, user_chats
from django.urls import path

urlpatterns = [
        path('', list_chats, name='list_chats'),
        path('<int:pk>', chat_list, name='chat_list'),
        path('new/', create_chat, name='create_chat'),
        path('<str:pk>', user_chats, name='user_chats'),
]
