from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(View):
    form_class = UserForm
    template_name = 'authentication/login.html'

    def get(self, request):

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("A")
            return render(request,'authentication/success.html' ) # need to add gruop attribute 
        else:
            print("B")
            return redirect('authentication:login')

class logoffView(View):
    pass

class SignUpView(View):
    pass

