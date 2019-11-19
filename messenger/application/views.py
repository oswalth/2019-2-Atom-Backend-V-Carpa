from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

def redirect_test(request, path):
    response = HttpResponse()
    response['X-Accel-Redirect'] = '/hidden/' + path
    print('python')
    print((response._headers))
    return response