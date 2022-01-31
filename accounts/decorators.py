from django.contrib.auth import decorators
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_funct):
    def wrapper_func(request,*args,**kwaargs):
        if request.user.is_authenticated:
            return redirect('homes')
        else:        
            return view_funct(request,*args,**kwaargs)
    
    return wrapper_func

def allowed_users(allowed_rules=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwaargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            
            if group in allowed_rules:
                return view_func(request,*args,**kwaargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_funct):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name

        if group=='customer':
            return redirect('homes')
        
        if group=='admin':
            return view_funct(request,*args,**kwargs)
    return wrapper_function