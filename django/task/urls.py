from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet) # 'tasks' will be the URL prefix
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls