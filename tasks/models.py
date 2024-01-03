from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    """
    Task model for details of the task assigned to someone/ self
    """
    STATUS_CHOICES = [
        (0, "Pending"),
        (1, "Executing"),
        (2, "Completed"),
        (3, "Blocked"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    assignees = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_assignee', default="")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task_project', default="")
    status = models.IntegerField(choices= STATUS_CHOICES, default=0)
    attachment = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.task_name}'
