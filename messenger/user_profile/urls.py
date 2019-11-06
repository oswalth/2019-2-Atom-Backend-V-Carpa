from user_profile.views import user_profile
from django.urls import path


urlpatterns = [
        path('', user_profile, name='user_profile'),
        path('<str:pk>', user_profile, name='user_profile'),
]
