from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contact_list(request, pk=None):
    if request.method in ('GET', 'POST'):
        if pk is None:
            return JsonResponse({'msg': 'enter user id'})
        return JsonResponse({'user id': pk, 'amount of contacts': 50,
                             'online': '24'})
    return JsonResponse(
        {'test': 'Wrong method {}'.format(request.method)}, status=400)
