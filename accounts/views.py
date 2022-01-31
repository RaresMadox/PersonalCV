from accounts.decorators import unauthenticated_user
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import Group

from .forms import CreateUserForm,UserForm
from .decorators import unauthenticated_user,allowed_users
from .models import Visit


from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
@allowed_users(allowed_rules=['admin','customer'])
def userPage(request):

    visit=request.user.visit
    form=UserForm(instance=visit)
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance=visit)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'accounts/user.html',context)

@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            #group=Group.objects.get(name='customer')
            #user.groups.add(group)
            # Visit.objects.create(
            #      user=user,
            #      name=user.username,
            #      email=user.email,            
            # )

            messages.success(request,'Account was created for '+username)
            return redirect('accounts:login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('accounts:login')

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
            
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('homes')
        else:
            messages.info(request,'Username Or Password is incorrect')
    context={}
    return render(request,'accounts/login.html',context)
# Create your views here.
# def signup_view(request):
#     if request.method =='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             #log the user
#             login(request,user)
#             return redirect('projects:list')
#     else:
#         form=UserCreationForm()
#     #form=UserCreationForm()
#     return render(request,'accounts/signup.html',{'form':form})

# def login_view(request):
#     if request.method =='POST':
#         form=AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # log in the user
#             user = form.get_user()
#             login(request,user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('projects:list')
#     else:
#         form=AuthenticationForm()
#     return render(request,'accounts/login.html',{'form':form})

# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect(' projects:list')