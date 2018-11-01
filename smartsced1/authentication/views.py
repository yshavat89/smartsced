from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
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
            return redirect('polls:question_add')
        else:
            return redirect('my_login:login')

class logoffView(View):
    pass

class SignUpView(View):
    pass

