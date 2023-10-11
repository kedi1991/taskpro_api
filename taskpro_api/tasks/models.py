from django.db import models
from django.contrib.auth.models import User
 
class Task(models.Model):
    """
    Task model for details of the task assigned to someone/ self
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    assignees = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    attachment = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.task_name}'

