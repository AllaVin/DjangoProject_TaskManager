"""
URL configuration for DjangoProject_TaskManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from django.urls import path

from TaskManager_app.views import test

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("task_manager/", view=test),
    path('TaskManager_app/', include('TaskManager_app.urls')), # http://127.0.0.1:8000/TaskManager_app/task_manager_path
]
