from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import  UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'An Account is created for '+ user + ' Please Log in Here')
                return redirect('/start_page/login')
        return render(request, 'users/register.html', {'form': form})
    
def login_page(request):
    if request.user.is_authenticated:
        return redirect('blog-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('blog-home')
            else:
                messages.info(request, 'Username or Password is Incorrect')


    form = UserCreationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('/start_page/login/')

