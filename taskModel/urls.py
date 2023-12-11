
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.taskForm,name='taskForm'),
    path('edit/<int:id>',views.editTask,name='editTask'),
]