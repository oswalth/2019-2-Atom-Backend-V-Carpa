from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import User
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404


@require_http_methods(["GET", "POST"])
@csrf_exempt
def user_profile(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter user id'})
    else:
        user = get_object_or_404(User, username=pk)
        return JsonResponse({'response': user.__str__()})
    return JsonResponse({'user id': pk, 'country': 'Uganda',
                        'status': 'online'})


def find_user(username):
    return User.objects.all().filter(username=username) or None
