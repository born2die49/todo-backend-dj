from rest_framework import serializers

from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['id',
      'task_name',
      'description',
      'add_date',
      'due_date',
      'duration_minutes',
      'status',
      'category',
      'task_type',
    ]