from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name = 'authentication/login.html'

class SignInView(View):
    pass

class SignOutView(View):
    pass

