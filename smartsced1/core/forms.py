from django import forms
from django.contrib.admin import widgets
from .models import Tasks, Products, Projects, ProjectInProduct, TaskInProject, Tips

class TasksForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(TasksForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Tasks
        fields = ['name','tType','risk','PRD','summary',]

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['prodName']

class ProjectsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(ProjectsForm, self).__init__(*args, **kwargs)
       self.fields['startTime'].widget = widgets.AdminSplitDateTime()
    class Meta:
        model = Projects
        fields = ['executorID','projectName','summary','startTime','status','numberOfTasks']

class ProjectInProductForm(forms.ModelForm):

    class Meta:
        model = ProjectInProduct
        fields = ['prodID','projectID','startTime','endTime','report']

class TaskInProjectForm(forms.ModelForm):

    class Meta:
        model = TaskInProject
        fields = ['projectID','taskID','report','exeID','startTime','endTime']

class TipsForm(forms.ModelForm):

    class Meta:
        model = Tips
        fields = ['taskID','tipTxt']

