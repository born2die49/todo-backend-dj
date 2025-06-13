from rest_framework import viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
  """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Tasks.
    """
  queryset = Task.objects.all().order_by('-add_date')
  serializer_class = TaskSerializer
  
class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset provides the same automatic actions for Categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer