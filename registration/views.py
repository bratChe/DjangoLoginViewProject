from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm
from django.contrib import messages


from django.contrib.auth import authenticate,login,logout

# Create your views here.
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request , username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    context={}
    return render(request , 'login\login.html',context)




def home(request):
     return render(request , 'login\logedin.html')
        



def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request , 'Account was created for ' + user)
            return redirect('login')
            
            
    context={'form':form}
    return render(request, 'login/register.html' , context)


