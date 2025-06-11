from django.contrib import admin
from TaskManager_app.models import Task, SubTask, Category, Project

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Project)

# Register your models here.
