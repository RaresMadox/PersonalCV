from django.urls import path,include
from . import views

app_name='projects'

urlpatterns = [
    
    path('',views.project_list,name="list"),
    path('create/',views.project_create,name="create"),
    path('<slug:slug>/',views.project_detail,name="detail"),
    path('<slug:slug>/edit/',views.project_edit,name="edit"),
    
    
]