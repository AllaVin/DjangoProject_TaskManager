from django.contrib import admin
from TaskManager_app.models import Task, SubTask, Category, Project

# admin.site.register(Category)
# admin.site.register(Task)
# admin.site.register(SubTask)
# admin.site.register(Project)

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',
                    "description",
                    'get_categories',
                    'status',
                    'project',
                    'priority',
                    'deadline',
                    'created_at',)
    search_fields = ('title',)
    ordering = ('title',)
    list_per_page = 5


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title',
                    "description",
                    'task',
                    'status',
                    'deadline',
                    'created_at',)
    search_fields = ('title',)
    ordering = ('title',)
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 5

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'description',
                    'created_at',)  # добавь нужные поля
    search_fields = ('name',)