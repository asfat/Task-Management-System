from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def taskcategory(request):
    form=forms.Category
    if request.method == 'POST':
        form=forms.Category(request.POST)
        if form.is_valid():
            form.save()
        return redirect('showtask')
    return render(request,'addtask.html',{'form':form})