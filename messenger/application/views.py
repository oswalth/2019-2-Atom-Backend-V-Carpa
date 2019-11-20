from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
import hmac
import base64
import hashlib
from .config import AWS
import boto3
from time import gmtime, strftime


def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha1).digest()


def download_file(request, path, filename):
    """response = HttpResponse()
    # response['X-Accel-Redirect'] = '/hidden/' + path
    aws_access = AWS['AWS_ACCESS_KEY_ID':]
    aws_secret = AWS['AWS_SECRET_ACCESS_KEY']

    string_to_sign = "{}\n\n\n".format(request.method)
    # response
    print('python')
    print((response._headers))
    return response
    if request.user.is_authenticated:
        if True:
            session = boto3.session.Session()
            s3_client = session.client(service_name='s3',
                                        endpoint_url=AWS['AWS_S3_ENDPOINT_URL'],
                                        aws_access_key_id=AWS['AWS_ACCESS_KEY_ID'],
                                        aws_secret_access_key=AWS['AWS_SECRET_ACCESS_KEY'],)
            
            url = s3_client.generate_presigned_url('get_object',
                Params = {
                    'Bucket': AWS['AWS_STORAGE_BUCKET_NAME'],
                    'Key' : 'users/{}/{}'.format(path, filename)
                })
            return JsonResponse({'file': url})
    else:
        return HttpResponseForbidden()"""


    if True: #request.user.is_authenticated:
        if True:
            aws_access = AWS['AWS_ACCESS_KEY_ID']
            aws_secret = AWS['AWS_SECRET_ACCESS_KEY']

            response = HttpResponse()
            response['X-Accel-Redirect'] = '/hidden/' + path

            url_full = request.path
            string_to_sign = "{}\n\n\n\nx-amz-date:{}".format(request.method, strftime("%H:%M:%S", gmtime()))

            signature = base64.urlsafe_b64encode(hmac.new(aws_secret, string_to_sign, hashlib.sha1).digest())

            response['authorization'] = 'AWS {}:{}'.format(aws_secret, signature)
            response['host'] = 'https://{}.hb.bizmrg.com'.format(AWS['AWS_STORAGE_BUCKET_NAME'])
            return response
    else:
        return HttpResponseForbidden()