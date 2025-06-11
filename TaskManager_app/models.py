from django.db import models

STATUS_CHOICES = [
    ('New', 'New'),
    ('In Progress', 'In Progress'),
    ('Pending', 'Pending'),
    ('Blocked', 'Blocked'),
    ('Done', 'Done'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='tasks')  # ✅ правильная связь
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')  # ✅ один-ко-многим
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
