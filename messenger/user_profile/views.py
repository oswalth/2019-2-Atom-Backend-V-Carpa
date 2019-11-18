from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import User
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .forms import NewUserForm
from django.shortcuts import render, render_to_response


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


@require_http_methods(["GET", "POST"])
@csrf_exempt
def add_user(request):
    """
    Функция, позволяющая поменять последнее прочитанное сообщение
    участника чата.
    """
    if request.method == 'POST':
        new_user_form = NewUserForm(request.POST, request.FILES)
        print('-'*50)
        print(request.FILES)
        if new_user_form.is_valid():
            new_user_form.save()
        else:
            print(new_user_form.errors)
    else:
        new_user_form = NewUserForm()
    return render_to_response(
        'new_user.html', {
            'new_user_form': new_user_form},)