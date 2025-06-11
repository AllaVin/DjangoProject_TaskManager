from django.contrib import admin
from TaskManager_app.models import Task, SubTask, Category



admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)

# Register your models here.
