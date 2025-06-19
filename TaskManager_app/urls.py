from django.urls import path
from .views import test

urlpatterns = [
    path('task_manager_path', view=test),  # # http://127.0.0.1:8000/TaskManager_app/task_manager_path
]
