from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser,models.Model):
    MANAGER = 'M'
    EDITOR = 'E'
    WORKER = 'W'
    GROUP_CHOICES = (
        (MANAGER, 'Manager'),
        (EDITOR, 'Editor'),
        (WORKER, 'Worker'),
    )
    group = models.CharField(max_length=2, choices=GROUP_CHOICES, default=WORKER)
    test = models.CharField(max_length=2)
    #image = models.ImageField(upload_to='treasure_image', default='media/default.png')
