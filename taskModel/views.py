from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.
def taskForm(request):
    form=forms.TaskForm
    if request.method == 'POST':
        form=forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('showtask')
    return render(request,'addtask.html',{'form':form})

def editTask(request, id):
    task_instance = models.TaskModel.objects.get(pk=id)
    edit_form = forms.TaskForm(instance=task_instance)

    if request.method == "POST":
        copy_form = forms.TaskForm(request.POST, instance=task_instance)
        if copy_form.is_valid():
            copy_form.save()
            return redirect('showtask')

    return render(request, 'addtask.html', {'form': edit_form})