from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_profile(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter user id'})
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'user id': pk, 'country': 'Uganda',
                            'status': 'online'})
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)})
