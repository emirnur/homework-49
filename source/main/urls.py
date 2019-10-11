"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, IssueView, IssueCreateView, IssueUpdateView, \
    IssueDeleteView, StatusView, StatusCreateView, StatusUpdateView, StatusDeleteView, TypeView,\
    TypeCreateView, TypeUpdateView, TypeDeleteView
from webapp.views.project_views import ProjectIndex, ProjectView, ProjectCreateView, ProjectUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
    path('issue/status/', StatusView.as_view(), name='status_view'),
    path('issue/status/add/', StatusCreateView.as_view(), name='status_add'),
    path('issue/status/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('issue/status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('issue/type/', TypeView.as_view(), name='type_view'),
    path('issue/type/add/', TypeCreateView.as_view(), name='type_add'),
    path('issue/type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('issue/type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    path('issue/project/', ProjectIndex.as_view(), name='project_index'),
    path('issue/project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('issue/project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('issue/project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
]
