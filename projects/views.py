from django.contrib.auth import forms
from django.shortcuts import get_object_or_404, render,redirect
from .models import Project
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateProject,UpdateProject
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib import messages

# Create your views here.
@login_required(login_url='accounts:login')
@allowed_users(allowed_rules=['admin','customer'])
def project_list(request):
    projects=Project.objects.all().order_by('published')
    return render(request,'projects/project_list.html',{'projects':projects})

@login_required(login_url='accounts:login')
def project_detail(request,slug):
    project=Project.objects.get(slug=slug)
    return render(request,'projects/project_detail.html',{'project':project})

@login_required(login_url='accounts:login')
@admin_only
def project_create(request):
    form=CreateProject()
    if request.method=='POST':
        form=CreateProject(request.POST)
        if form.is_valid():
            form.save()
            title=request.POST.get('title')
            descrtion=request.POST.get('descrtion')
            slug=request.POST.get('slug')
            thumb=request.POST.get('thumb')
            thumb1=request.POST.get('thumb1')
            thumb2=request.POST.get('thumb2')
            thumb3=request.POST.get('thumb3')
            category=request.POST.get('category')
            category2=request.POST.get('category2')
            tags=request.POST.get('tags')

            messages.success(request,'The projest has been added ')
            return redirect('projects:list')
    context={'form':form}
    return render(request,'projects/project_create.html',context)
  
@login_required(login_url='accounts:login')
def project_edit(request,slug):
    
    if request.method =="POST":
        project_acc=Project.objects.get(slug=slug)
        form=UpdateProject(request.POST or None,request.FILES, instance=project_acc)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'projects/project_edit.html',context)