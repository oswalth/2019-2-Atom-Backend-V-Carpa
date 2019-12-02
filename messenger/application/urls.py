"""messenger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('templates.urls')),
    path('file/<path>/<filename>', views.download_file),
    path('admin/', admin.site.urls),
    # path('chats/', include('chats.urls')),
    # path('contacts/', include('contact_list.urls')),
    # path('chatpage/', include('chat_page.urls')),
    # path('profile/', include('user_profile.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/chats/', include('chats.api.urls')),
    path('api/users/', include('user_profile.api.urls')),
    path('api/messages/', include('message.api.urls')),
]
