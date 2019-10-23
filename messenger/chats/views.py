from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat_list(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter chat_id'})
    if request.method == 'POST':
        return JsonResponse({'chat_id': pk, 'members': 200})
    elif request.method == 'GET':
        return JsonResponse({'chat_id': pk, 'members': 200})
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)})
