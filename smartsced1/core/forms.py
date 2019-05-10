from django import forms
from .models import Tasks, Products, Projects, ProjectInProduct, TaskInProject, Tips

class TasksForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
       super(TasksForm, self).__init__(*args, **kwargs)
       self.fields['ownerID'].widget.attrs['readonly'] = True

    class Meta:
        model = Tasks
        fields = ['ownerID','summary','tType','risk','name','PRD']

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['prodName','ownerID']

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ['ownerID','executorID','projectName','summary','startTime','status','numberOfTasks']

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
        fields = ['taskID','ownerID','tipTxt']

