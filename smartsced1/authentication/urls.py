from django.urls import path

from . import views

app_name = 'authentication' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),

]