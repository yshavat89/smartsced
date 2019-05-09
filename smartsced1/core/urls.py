from django.urls import path

from . import views

app_name = 'core' # namespacing: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#namespacing-url-names 
urlpatterns = [
    path('task/add', views.CreateTasksView.as_view(), name='task-add'),
    path('taskinproject/add', views.CreateTaskInProjectView.as_view(), name='taskinproject-add'),
    path('project/add', views.CreateProjectsView.as_view(), name='project-add'),
    path('tip/add', views.CreateTipsView.as_view(), name='tip-add'),
    path('projectinproduct/add', views.CreateProjectInProductView.as_view(), name='projectinproduct-add'),
    path('product/add', views.CreateProductsView.as_view(), name='product-add'),
]
