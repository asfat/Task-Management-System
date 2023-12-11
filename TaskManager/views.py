from django.shortcuts import render
from taskModel import models

def home(request):
    return render(request,'base.html')

def showtask(request):
    task_list=models.TaskModel.objects.all()
    print(task_list)
    for i in task_list:
        print(i.is_completed)
        task_category=i.task_category.all()
        # for j in task_category:
        #     print(j.category)
    return render(request,'showtask.html',{'task_list':task_list})