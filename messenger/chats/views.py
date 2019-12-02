# from django.http import JsonResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# from django import forms
# from .models import Chat
# from django.shortcuts import render, render_to_response
# from user_profile.models import User, Member
# from django.views.decorators.http import require_http_methods
# from .forms import UserReadMessageForm, NewMessageForm, NewChatForm, MembersForm


# @require_http_methods(["GET", "POST"])
# @csrf_exempt
# def chat_list(request, pk=None):
#     """
#     Функция выводит описание и список сообщений по id чата
#     /chats/<int:pk>
#     """
#     if pk is None:
#         return JsonResponse({'msg': 'enter chat_id'})
#     response = {}
#     messages = list(Message.objects.filter(chat=pk).values())
#     if not Chat.objects.filter(id=pk):
#         return JsonResponse({'ERR': 'Chat#{} not found'.format(pk)})
#     if not messages:
#         return JsonResponse({'ERR': 'No messages yet for chat#{}'.format(pk)})
#     """for message in messages:
#         response['message#{}'.format(message['id'])] = message"""
#     return JsonResponse({
#         'chat#{}-info'.format(pk): Chat.objects.filter(id=pk).values()[0],
#         'messages': [message for message in messages]
#     })





# @require_http_methods(["GET", "POST"])
# @csrf_exempt
# def create_chat(request):
#     """
#     Функция, которая позволяет создать чат. Оперирует формой,
#     описанной выше.
#     """
#     print((request.COOKIES))
#     if request.method == 'POST':
#         members = []
#         chat_form = NewChatForm(request.POST)
#         members_form = MembersForm(request.POST)
#         if chat_form.is_valid() and members_form.is_valid():
#             current_chat = chat_form.save()
#             not_host = members_form.save(commit=False)
#             not_host.chat = current_chat
#             not_host.save()
#             Member.objects.create(user=current_chat.host, chat=current_chat)
#     else:
#         chat_form = NewChatForm()
#         members_form = MembersForm()
#     return render_to_response(
#         'new_chat.html', {
#             'chat_form': chat_form, 'members_form': members_form},)


# @require_http_methods(["GET", "POST"])
# @csrf_exempt
# def user_chats(request, pk=None):
#     """
#     Функция, позволяющая вывести список всех чатов пользователя,
#     обозначенного через его username
#     /chats/<str:pk>
#     """
#     if pk is None:
#         return JsonResponse({'msg': 'specify user id'})
#     user = User.objects.all().filter(username=pk)[0]
#     membership = Member.objects.all().filter(user=user.id)
#     chats = []
#     for member in membership:
#         chats.append(member.chat)
#     response = dict()
#     for chat in chats:
#         response['chat#{}'.format(chat.id)] = {
#             'user': user.username,
#             'is_group': chat.is_group_chat,
#             'topic': chat.topic or 'No topic',
#             'host': chat.host.username,
#         }
#     return JsonResponse(response)


# @require_http_methods(["GET", "POST"])
# @csrf_exempt
# def list_chats(request):
#     """
#     Функция, выводящая список всех имеющихся чатов
#     """
#     response = dict()
#     chats = Chat.objects.all()
#     for chat in chats:
#         response['chat#{}'.format(chat.id)] = {
#             'title': chat.title,
#             'is_group': chat.is_group_chat,
#             'topic': chat.topic or 'No topic',
#             'host': chat.host.username,
#         }
#     return JsonResponse(response)



# @require_http_methods(["GET", "POST"])
# @csrf_exempt
# def send_message(request, pk):
#     """
#     Функция, позволяющая отправить сообщение
#     /chats/<int:pk>/new
#     """
#     if not Chat.objects.filter(id=pk):
#         return JsonResponse({'ERR': 'Chat#{} is not found'.format(pk)})
#     variants = [x.user.id for x in Member.objects.filter(chat=pk)]
#     if request.method == 'POST':
#         message_form = NewMessageForm(request.POST)
#         if message_form.is_valid():
#             tmp_form = message_form.save(commit=False)
#             current_chat = Chat.objects.filter(id=pk)[0]
#             tmp_form.chat = current_chat
#             tmp_form.save()
#             sender = Member.objects.filter(user=tmp_form.sender, chat=current_chat)[0]
#             sender.last_read_message = tmp_form
#             sender.save()
#             current_chat.last_message = tmp_form
#             current_chat.save()
#             message_form = NewMessageForm()
#             message_form.fields['sender'].queryset = User.objects.filter(
#                 id__in=variants)
#     else:
#         message_form = NewMessageForm()
#         message_form.fields['sender'].queryset = User.objects.filter(
#             id__in=variants)
#     return render_to_response(
#         'new_message.html', {
#             'message_form': message_form},)



# @require_http_methods(["GET", "POST"])
# @csrf_exempt
# def read_message(request, pk):
#     """
#     Функция, позволяющая поменять последнее прочитанное сообщение
#     участника чата.
#     """
#     if request.method == 'POST':
#         user_read_form = UserReadMessageForm(request.POST)
       
#         if user_read_form.is_valid():
#             message_id = user_read_form.cleaned_data['message_to_read']
#             tmp_form = user_read_form.save(commit=False)
#             user, chat = tmp_form.user, Chat.objects.filter(id=pk)[0]
#             member = Member.objects.all().filter(user=user, chat=chat)[0]
#             member.last_read_message = Message.objects.filter(id=message_id)[0]
#             member.save()
#     else:
#         user_read_form = UserReadMessageForm()
#         variants = [x.user.id for x in Member.objects.filter(chat=pk)]
#         user_read_form.fields['user'].queryset = User.objects.filter(
#             id__in=variants)
#     return render_to_response(
        # 'read_message.html', {
        #     'user_read_form': user_read_form},)
