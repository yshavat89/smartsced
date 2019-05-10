from django.db import models
from authentication.models import User
#from matrix_field import MatrixField

class Products(models.Model):
    prodName = models.CharField("product name",max_length=128)
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.prodName
    


class Projects(models.Model):
    C1 = 'C1'
    C2 = 'C2'
    C3 = 'C3'
    C4 = 'C4'
    PROJECT_STATUS_CHOICES = (
        (C1, 'STARTED'),
        (C2, 'SUSPENDED'),
        (C3, 'FUTURE'),
        (C4, 'ENDED'),
    )
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Project_owner')#PFK
    executorID = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name = u'executor',) # NULL allowed, but must be filled out in a form
    projectName = models.CharField("project name",max_length=128)
    creationTime = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=128)
    startTime = models.DateTimeField("start time",auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=2,choices=PROJECT_STATUS_CHOICES,default=C1,)
#    dependencyMatrix =ArrayField(ArrayField(models.ImageField()))
#    dependencyMatrix = MatrixField()#datatype='int', dimensions=(100, 100)
    numberOfTasks = models.PositiveIntegerField(default=1) # validetors = [max_value = 100, min_value = 1])

    def __str__(self):
        return self.projectName
    

         
class ProjectInProduct(models.Model):
    prodID = models.ForeignKey(Products, on_delete=models.CASCADE) #PFK
    projectID = models.ForeignKey(Projects, on_delete=models.CASCADE)#PFK
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    report = models.CharField(max_length=128)

class Tasks(models.Model):
    TASK_TYPE_CHOICES = (
        ('C1', 'Manual'), #need to add to hover  " the task should be done manually by the worker from start to finish."
        ('C2', 'Automatic not batchable'),#need to add to hover  " the task is not done by the worker, but the worker has to press execute (launch it)."
        ('C3', 'Automatic batchable'),#need to add to hover "the task can be put as batch, run during the night without any user interference."
    )
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)#PFK
    lastModified = models.DateTimeField(auto_now=True)
    summary = models.TextField(max_length=128,)
    tType = models.CharField("type",max_length=2,choices=TASK_TYPE_CHOICES,default='C1',)
    risk = models.IntegerField(default=1,)# max_value = 10, min_value = 1)
    name = models.CharField(max_length=128)
    PRD = models.FileField("PDF file",upload_to='uploads/')

    def __str__(self):
        return self.name

class TaskInProject(models.Model):
    projectID =  models.ForeignKey(Projects, on_delete=models.CASCADE)
    taskID =  models.ForeignKey(Tasks, on_delete=models.CASCADE)
    report = models.CharField(max_length=128)
    exeID = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    endTime = models.DateTimeField(auto_now=False, auto_now_add=False)

class Tips(models.Model):
    taskID = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    tipTxt = models.CharField(max_length=128)


class B(models.Model):
    name = models.CharField(max_length=50)


class A(models.Model):
    b = models.ManyToManyField(B)
    name = models.CharField(max_length=50)


class C(models.Model):
    a = models.ForeignKey(A, on_delete=models.CASCADE)

# class HandField(models.Field):

#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = 104
#         super().__init__(*args, **kwargs)

#     def deconstruct(self):
#         name, path, args, kwargs = super().deconstruct()
#         del kwargs["max_length"]
#         return name, path, args, kwargs

# class Hands(models.Model):
#     hand = HandField()