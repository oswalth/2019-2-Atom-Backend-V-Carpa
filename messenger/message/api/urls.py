from message.api.views import MessageViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', MessageViewSet, basename='message')
urlpatterns = router.urls