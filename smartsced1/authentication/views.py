from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from .forms import UserForm, User, UserCreateForm
from django.contrib.auth import authenticate, login, logout
from .models import User

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
            print(username)
            return render(request,user.get_user_group() + '/success.html' ) # need to add gruop attribute 
        else:
            return redirect('authentication:login')

class logoffView(View):
    def get(self, request):
        logout(request)
        return redirect('authentication:login')

class SignUpView(View):
    form_class = UserCreateForm
    template_name = 'authentication/signup_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process from data
    def post(self, request):
        form = self.form_class(data=request.POST,files=request.FILES)

        if form.is_valid():
            user = form.save(commit=False)

            # clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    print("user is not None & active")
                    return redirect('authentication:login')
            print("user is not None & NOT active")
        print("user is NOT valid")
        return render(request, self.template_name, {'form': form})


