from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self): # This is helpful for representing the object in Django admin or shell
        return self.name

class Task(models.Model):
    # --- Basic Info ---
    task_name = models.CharField(max_length=200) 
    description = models.TextField(blank=True, null=True) 

    # --- Dates ---
    add_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True) 

    # --- Details ---
    duration_minutes = models.IntegerField(null=True, blank=True, help_text="Duration in minutes")

    # --- Status ---
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    TYPE_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
    ]
    task_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='personal',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.task_name