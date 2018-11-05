from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authentication' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logoff/', views.logoffView.as_view(), name='logoff'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)