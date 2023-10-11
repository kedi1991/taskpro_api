from django.db import models
from django.contrib.auth.models import User


 
class Project(models.Model):
    """
    Project model for details of the project the user is working on
    """
    owner = models.ForeignKey(Tas, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.project_name}'

