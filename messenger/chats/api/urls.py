# from chats.api.views import ChatViewSet
# from rest_framework.routers import DefaultRouter
# from django.urls import path, include


# router = DefaultRouter()
# router.register(r'', ChatViewSet, basename='chat')
# urlpatterns = router.urls
# print(urlpatterns)



from django.urls import path
from .views import (
    ChatDetailView,
    ChatListView,
    ChatCreateView,
    ChatUpdateView,
    ChatDeleteView,
)


urlpatterns = [
    path('', ChatListView.as_view()),
    path('<int:pk>/', ChatDetailView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>/update', ChatUpdateView.as_view()),
    path('<pk>/delete', ChatDeleteView.as_view()),
]
