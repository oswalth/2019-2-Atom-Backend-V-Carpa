from django import forms
from .models import Chat, Message
from user_profile.models import Member


class NewChatForm(forms.ModelForm):
    """
    Форма модели Chat, которая позволяет создать новый чат
    """
    # member = forms.
    class Meta:
        model = Chat
        fields = ('title', 'is_group_chat', 'topic', 'host')

    def clean_topic(self):
        """
        Функция проверяет, что Тема чата - буквенная строка,
        иначе все не буквенные символы удалятся из строки
        """
        if self.cleaned_data['topic'].isalpha():
            return self.cleaned_data['topic']
        return ''.join([x for x in self.cleaned_data['topic'] if x.isalpha()])


class MembersForm(forms.ModelForm):
    """
    Форма модели Member, позволяющая выбрать участников чата
    """
    class Meta:
        model = Member
        fields = ('user',)


class NewMessageForm(forms.ModelForm):
    """
    Форма модели Message, позволяющая добавить сообщение.
    """

    class Meta:
        model = Message
        fields = ('sender', 'content',)

    def clean_content(self):
        if self.cleaned_data['content'][0].isupper():
            return self.cleaned_data['content']
        return 'Введите сообщение'




class UserReadMessageForm(forms.ModelForm):
    """
    Форма модели Member, позволяющая выбрать участника чата,
    который читает сообщение
    """
    message_to_read = forms.CharField()

    class Meta:
        model = Member
        fields = ('user',)