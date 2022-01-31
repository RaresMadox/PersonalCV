from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from itertools import chain
# Create your views here.
from projects.models import Project,Tag
def home(request):
    Tags=Tag.objects.all().order_by('name')
    Category=Project.objects.all().order_by('title')
       
    return render(request, 'base/home.html',{'Tags':Tags,'Category':Category})
    

@login_required(login_url='accounts:login')
def search_cont(request):        
    if request.method=='POST':
        searched = request.POST.get('searched',False)
        result=Project.objects.filter(title__contains=searched)
        return render(request,'base/search_project.html',{'searched':searched,'result':result})
    else:
        return render(request,'base/search_project.html',{})

@login_required(login_url='accounts:login')
def search_tag(request): 
    if request.method=='POST':
        tag_src = request.POST.get('tag_src',False)

        result=Project.objects.filter(tags__name__contains=tag_src)
        return render(request,'base/search_tags.html',{'tag_src':tag_src,'result':result})
    else:
        return render(request,'base/search_tags.html',{})


@login_required(login_url='accounts:login')
def search_category(request): 
    if request.method=='POST':
        category_src = request.POST.get('category_src',False)
        
        result=Project.objects.filter(category__contains=category_src)
        
        return render(request,'base/search_category.html',{'category_src':category_src,'result':result})
    else:
        return render(request,'base/search_category.html',{})
    
           
        




 
