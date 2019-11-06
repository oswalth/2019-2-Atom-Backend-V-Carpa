from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import Chat
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from user_profile.models import User, Member


@csrf_exempt
def chat_list(request, pk=None):
    if request.method in ('GET', 'POST'):
        if pk is None:
            return JsonResponse({'msg': 'enter chat_id'})
        return JsonResponse({'chat_id': pk, 'members': 200})
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)})


class NewChatForm(forms.ModelForm):
    """OPTIONS = User.objects.all().values_list('username')
    members = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)"""
    # member = forms.
    class Meta:
        model = Chat
        fields = ('title', 'is_group_chat', 'topic', 'host')


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user',)


@csrf_exempt
def create_chat(request):
    if request.method == 'POST':
        members = []
        form = NewChatForm(request.POST)
        form2 = MembersForm(request.POST)
        if form.is_valid() and form2.is_valid():
            current_chat = form.save()
            not_host = form2.save(commit=False)
            not_host.chat = current_chat
            not_host.save()
            Member.objects.create(user=current_chat.host, chat=current_chat)
    else:
        form = NewChatForm()
        form2 = MembersForm()
    return render_to_response('new_chat.html', {'form': form, 'form2': form2},)


def user_chats(request, pk=None):
    if request.method in ('GET', 'POST'):
        if pk is None:
            return JsonResponse({'msg': 'specify user id'})
        user = User.objects.all().filter(username=pk)[0]
        membership = Member.objects.all().filter(user=user.id)
        chats = []
        for member in membership:
            chats.append(member.chat)
        response = dict()
        for chat in chats:
            response['chat#{}'.format(chat.id)] = {
                'user': user.username,
                'is_group': chat.is_group_chat,
                'topic': chat.topic or 'No topic',
                'host': chat.host.username,
            }
        return JsonResponse(response)
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)})


def list_chats(request):
    response = dict()
    chats = Chat.objects.all()
    for chat in chats:
            response['chat#{}'.format(chat.id)] = {
                'title': chat.title,
                'is_group': chat.is_group_chat,
                'topic': chat.topic or 'No topic',
                'host': chat.host.username,
            }
    return JsonResponse(response)
