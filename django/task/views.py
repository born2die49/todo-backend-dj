from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
  """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Tasks.
    """
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
      """
      This view should return a list of all the tasks
      for the currently authenticated user.
      """
      # The `request.user` is the User instance that is making the request.
      return Task.objects.filter(owner=self.request.user).order_by('-add_date')

  def perform_create(self, serializer):
      """
      Assign the current user as the owner of the task when it's created.
      """
      # When we save the serializer, we pass the owner from the request.
      serializer.save(owner=self.request.user)
  
class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset provides the same automatic actions for Categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer