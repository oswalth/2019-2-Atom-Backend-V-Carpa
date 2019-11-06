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
        chat = Chat.objects.get(id=chat_id)
        sender = User.objects.get(id=user_id)
        message = Message.objects.create(chat=chat, sender=sender, content=content)


def fill_users():
    from user_profile.models import User, Member
    infos = (('Vladimir Putin', 'tsar'),
             ('Donald Trump', 'lil_trump'),
             ('Xi Jinping', 'winnie_pooh'))
    for name, nick in infos:
        first_name = name.split()[0]
        last_name = name.split()[1]
        usr = User.objects.create(username=nick, last_name=last_name, first_name=first_name, avatar='tmp_url')


def fill_chats():
    from user_profile.models import User
    from chats.models import Chat
    for usr in User.objects.all():
        if usr.id == 3:
            chat = Chat.objects.create(
                is_group_chat=True,
                host=usr,
                title='No money, No honey!')
        else:
            chat = Chat.objects.create(
                is_group_chat=False,
                host=usr,
                title='{} private'.format(
                    usr.username))


def fill_members():
    from user_profile.models import User, Member
    from chats.models import Chat
    members = ((1, 1), (2, 1), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3))
    for user_id, chat_id in members:
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(id=chat_id)
        member = Member.objects.create(user=user, chat=chat, last_read_message=None)


def fill_attachemnets():
    from chats.models import Chat, Message, Attachment
    filling_template = {
        1: 3,
        2: 0,
        3: 2
    }
    for chat_id, att_numb in filling_template.items():
        chat = Chat.objects.get(id=chat_id)
        message = Message.objects.get(id=chat_id)
        for i in range(att_numb):
            url = 'https://chat#{}-attachement#{}.com'.format(chat_id, i)
            attachment = Attachment.objects.create(
                chat=chat,
                message=message,
                attachment_type='photo',
                url=url)


fill_users()
fill_chats()
fill_members()
fill_messages()
fill_attachemnets()
