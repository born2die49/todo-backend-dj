from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task') # 'tasks' will be the URL prefix
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls