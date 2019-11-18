from user_profile.views import user_profile, add_user
from django.urls import path


urlpatterns = [
        path('', user_profile, name='user_profile'),
        path('register/', add_user, name='add_user'),
        path('<str:pk>', user_profile, name='user_profile'),
]
