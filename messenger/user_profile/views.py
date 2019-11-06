from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import User


@csrf_exempt
def user_profile(request, pk=None):
    if request.method in ('GET', 'POST'):
        if pk is None:
            return JsonResponse({'msg': 'enter user id'})
        else:
            user = find_user(pk)[0]
            if user is None:
                return JsonResponse({'response': 'user not found'})
            else:
                return JsonResponse({'response': user.__str__()})
        return JsonResponse({'user id': pk, 'country': 'Uganda',
                            'status': 'online'})
    return JsonResponse({'test': 'Wrong method {}'.format(request.method)}, status=404)


def find_user(username):
    return User.objects.all().filter(username=username) or None
