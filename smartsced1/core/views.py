from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TasksForm , TaskInProjectForm, ProjectsForm, TipsForm, ProjectInProductForm, ProductsForm
from .models import Tasks, TaskInProject, Projects, Tips, ProjectInProduct, Products
from authentication.models import User

class CreateTasksView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = TasksForm
    template_name = 'Tasks/tasks_form.html'
   

    # display blank form
    def get(self, request):
        form = self.form_class({'ownerID':request.user},None)
        task_objects = get_list_or_404(Tasks)
        project_objects = get_list_or_404(Projects)

        return render(request, self.template_name, {'form': form, 'task_list':task_objects, 'project_list': project_objects})

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST,files=request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.ownerID = request.user
            task.save()
        return redirect('core:task-add')


class CreateTaskInProjectView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = TaskInProjectForm
    template_name = 'TaskInProject/taskinproject_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save(commit=True)
        return render(request, 'TaskInProject/index.html')

class CreateProjectsView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = ProjectsForm
    template_name = 'Projects/projects_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST,files=request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.ownerID = request.user
            project.save()
        return render(request, 'Projects/index.html')

class CreateTipsView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = TipsForm
    template_name = 'Tips/tips_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
       # form.owner = User.objects.filter(user_pk=)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST,files=request.FILES)
            
        if form.is_valid():
            tip = form.save(commit=False)
            tip.ownerID = request.user
            tip.save()
        return render(request, 'Tips/index.html')

class CreateProjectInProductView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = ProjectInProductForm
    template_name = 'ProjectInProduct/projectinproduct_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save(commit=True)
        return render(request, 'ProjectInProduct/index.html')

class CreateProductsView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = ProductsForm
    template_name = 'Products/products_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
       # form.owner = User.objects.filter(user_pk=)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.ownerID = request.user
            product.save()
        return render(request, 'Products/index.html')

class CreateTasks2View(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = TasksForm
    model = Tasks
    template_name = 'Tasks/tasks_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
       # form.owner = User.objects.filter(user_pk=)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save(commit=True)
        return render(request, 'Tasks/index.html')


# class CreateTasksView(LoginRequiredMixin, View):
#     # login_url this values handele auth and redirects if user is not logs in 
#     # hear the redirection is to the / path
#     login_url = '/'
#     redirect_field_name = 'redirect_to'

#     # View
#     form_class = TasksForm
#     template_name = 'Tasks/tasks_form.html'

#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#        # form.owner = User.objects.filter(user_pk=)
#         return render(request, self.template_name, {'form': form, })

#     # process from data
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#         return render(request, 'Tasks/index.html')


# class CreateTasksView(LoginRequiredMixin, View):
#     # login_url this values handele auth and redirects if user is not logs in 
#     # hear the redirection is to the / path
#     login_url = '/'
#     redirect_field_name = 'redirect_to'

#     # View
#     form_class = TasksForm
#     template_name = 'Tasks/tasks_form.html'

#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#        # form.owner = User.objects.filter(user_pk=)
#         return render(request, self.template_name, {'form': form, })

#     # process from data
#     def post(self, request):
#         form = self.form_class(data=request.POST,files=request.FILES)

#         if form.is_valid():
#             form.save(commit=True)
#         return render(request, 'Tasks/index.html')


# class CreateTasksView(LoginRequiredMixin, View):
#     # login_url this values handele auth and redirects if user is not logs in 
#     # hear the redirection is to the / path
#     login_url = '/'
#     redirect_field_name = 'redirect_to'

#     # View
#     form_class = TasksForm
#     template_name = 'Tasks/tasks_form.html'

#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#        # form.owner = User.objects.filter(user_pk=)
#         return render(request, self.template_name, {'form': form, })

#     # process from data
#     def post(self, request):
#         form = self.form_class(data=request.POST,files=request.FILES)

#         if form.is_valid():
#             form.save(commit=True)
#         return render(request, 'Tasks/index.html')


# class CreateTasksView(LoginRequiredMixin, View):
#     # login_url this values handele auth and redirects if user is not logs in 
#     # hear the redirection is to the / path
#     login_url = '/'
#     redirect_field_name = 'redirect_to'

#     # View
#     form_class = TasksForm
#     template_name = 'Tasks/tasks_form.html'

#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#        # form.owner = User.objects.filter(user_pk=)
#         return render(request, self.template_name, {'form': form, })

#     # process from data
#     def post(self, request):
#         form = self.form_class(data=request.POST,files=request.FILES)

#         if form.is_valid():
#             form.save(commit=True)
#         return render(request, 'Tasks/index.html')


# class CreateTasksView(LoginRequiredMixin, View):
#     # login_url this values handele auth and redirects if user is not logs in 
#     # hear the redirection is to the / path
#     login_url = '/'
#     redirect_field_name = 'redirect_to'

#     # View
#     form_class = TasksForm
#     template_name = 'Tasks/tasks_form.html'

#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#        # form.owner = User.objects.filter(user_pk=)
#         return render(request, self.template_name, {'form': form, })

#     # process from data
#     def post(self, request):
#         form = self.form_class(data=request.POST,files=request.FILES)

#         if form.is_valid():
#             form.save(commit=True)
#         return render(request, 'Tasks/index.html')
 