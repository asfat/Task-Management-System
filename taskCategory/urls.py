from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.taskcategory,name='taskcategory'),
]