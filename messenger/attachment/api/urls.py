from attachment.api.views import AttachmentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', AttachmentViewSet, basename='attachment')
urlpatterns = router.urls