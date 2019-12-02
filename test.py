import requests
import django 

print("hello world")

"""if __name__ == '__main__':
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url=AWS['AWS_S3_ENDPOINT_URL'],
                                aws_access_key_id=AWS['AWS_ACCESS_KEY_ID'],
                                aws_secret_access_key=AWS['AWS_SECRET_KEY_ID'],)
    
    s3_client.put_object(Bucket=AWS['AWS_STORAGE_BUCKET_NAME'], 
                            Key='user#1/1234', 
                            Body='Hello, World!')
                            
                            
from chats.models import Chat
chat = Chat(title='avatar chat', is_group_chat=False)
chat.avatar = ImageFile(open('user.jpg', 'rb'))
chat.save()
                       
from user_profile.models import User
from django.core.files.images import ImageFile

user = User(first_name='V', last_name='C', username='O')
user.avatar = ImageFile(open('user.jpg', 'rb'))
user.save()
                        
                            """