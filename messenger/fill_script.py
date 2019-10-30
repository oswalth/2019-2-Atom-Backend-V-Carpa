from user_profile.models import User, Member
from chats.models import Chat, Message


def fill_messages():
    from user_profile.models import User
    from chats.models import Chat, Message
    chat_user = ((1, 1), (1, 2), (2, 2), (3, 3), (3, 3), (3, 1))
    for chat_id, user_id in chat_user:
        if chat_id == 3:
            reciever = 'grp{}'.format(chat_id)
        else:
            reciever = 'usr'
        content = 'from usr{} to {}'.format(user_id, reciever)
        chat = Chat.objects.raw(
            'Select id FROM chats_chat WHERE id={}'.format(chat_id))[0]
        sender = User.objects.raw(
            'Select id FROM user_profile_user WHERE id={}'.format(user_id))[0]
        message = Message(chat=chat, sender=sender, content=content)
        message.save()


def fill_users():
    from user_profile.models import User, Member
    infos = (('Vladimir Putin', 'tsar'),
             ('Donald Trump', 'lil_trump'),
             ('Xi Jinping', 'winnie_pooh'))
    for name, nick in infos:
        usr = User(name=name, nick=nick, avatar='tmp_url')
        usr.save()


def fill_chats():
    from user_profile.models import User
    from chats.models import Chat
    for usr in User.objects.raw('Select * from user_profile_user'):
        if usr.id == 3:
            chat = Chat(
                is_group_chat=True,
                host=usr,
                title='No money, No honey!')
        else:
            chat = Chat(
                is_group_chat=False,
                host=usr,
                title='{} private'.format(
                    usr.nick))
        chat.save()


def fill_members():
    from user_profile.models import User, Member
    from chats.models import Chat
    members = ((1, 1), (2, 1), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3))
    for user_id, chat_id in members:
        user = User.objects.raw(
            'SELECT id from user_profile_user WHERE id={}'.format(user_id))[0]
        chat = Chat.objects.raw(
            'SELECT id from chats_chat WHERE id={}'.format(chat_id))[0]
        member = Member(user=user, chat=chat, last_read_message=None)
        member.save()


def fill_attachemnets():
    from chats.models import Chat, Message, Attachment
    filling_template = {
        1: 3,
        2: 0,
        3: 2
    }
    for chat_id, att_numb in filling_template.items():
        chat = Chat.objects.raw(
            'SELECT id from chats_chat WHERE id={}'.format(chat_id))[0]
        message = Message.objects.raw(
            'Select id from chats_message WHERE id={}'.format(chat_id))[0]
        for i in range(att_numb):
            url = 'https://chat#{}-attachement#{}.com'.format(chat_id, i)
            attachment = Attachment(
                chat=chat,
                message=message,
                attachment_type='photo',
                url=url)
            attachment.save()


fill_users()
fill_chats()
fill_members()
fill_messages()
fill_attachemnets()
