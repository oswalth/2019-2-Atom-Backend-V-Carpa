from chats.views import chat_list, create_chat, list_chats
from django.urls import path

urlpatterns = [
        path('', chat_list, name='chat_list'),
        path('<int:pk>', chat_list, name='chat_list'),
        path('new/', create_chat, name='create_chat'),
        path('usr_chats/<str:pk>', list_chats, name='list_chats'),
]
