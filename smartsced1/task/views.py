from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from .models import Task

class TaskFormView(LoginRequiredMixin, View):
    # login_url this values handele auth and redirects if user is not logs in 
    # hear the redirection is to the / path
    login_url = '/'
    redirect_field_name = 'redirect_to'

    # View
    form_class = TaskForm
    template_name = 'task/task_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, })

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST,files=request.FILES)

        if form.is_valid():
            form.save(commit=True)
        task_list = Task.objects.all()
        return render(request, 'task/index.html', {'task_list': task_list})
