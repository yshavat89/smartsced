from django.urls import path

from . import views

app_name = 'authentication' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logoff/', views.logoffView.as_view(), name='logoff'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    

]