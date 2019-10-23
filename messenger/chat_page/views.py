from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat_page(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter chat page id'})
    if request.method == 'POST' or request.method == 'GET':
        return JsonResponse({'chat page id': pk, 'amount of messages': 200,
                            'last_msg': '10:44'})
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)})
