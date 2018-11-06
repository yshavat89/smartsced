from django.db import models
from authentication.models import User

class Task(models.Model):
    
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=100)
    task_file = models.FileField(upload_to='taskfile')
    
    def __str__(self):
        return self.name