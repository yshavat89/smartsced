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
    phone = models.CharField(max_length=10,null=True,default=None)
    department = models.CharField(max_length=10,null=True,default='generic')
    image = models.ImageField(upload_to='user_image', default='user_image/default-user.jpg', )

    def get_user_group(self):
        for x in self.GROUP_CHOICES:
            if self.group in x:
                return x[1]
    
