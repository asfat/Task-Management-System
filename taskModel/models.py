from django.db import models
from taskCategory.models import TaskCategory
# Create your models here.
class TaskModel(models.Model):
    taskTitle= models.CharField(max_length=30)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    task_assign= models.DateField()
    task_category=models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle