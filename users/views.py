from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm, PasswordResetForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserRegistrationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import *

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:               
                auth_login(request, user)
                messages.success(request, "You have been successfully logged in.")
                return redirect('twitter-home')
            else:
                messages.error(request, 'Username or password is invalid.')
    form = AuthenticationForm()
    return render(request, 'users/login.html', context={'form': form})

def register(request): 
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get('email')
                form.save()
                username = form.cleaned_data.get('username')
                id = User.objects.get(username = username).id
                send_mail('Activate your account on Twitter', 
                f'Please follow the link below to activate your account http://localhost:8080/users/activate/{id}',
                 'tech.matrix.learner@gmail.com', 
                 [form.cleaned_data.get('email')])
                messages.success(request, f'User {username} has been successfully created.')
                return redirect('twitter-home')
            except IntegrityError:
                  messages.error(request, f'A user with the same email {email} already exists.')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', context={'form': form})


def activate(request,id):
    if id:
        User.objects.filter(pk=id).update(is_staff=True)
        messages.success(request, f'Your account has been successfully activated, you can login now.')
    else:
        messages.error(request, f'Something went wrong, please try again activating your account.')
    return redirect('twitter-home')
    

def reset_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            id = User.objects.get(email=email).id
            send_mail('Reset your Twitter password', 
            f'Please follow the link below to reset the password of your account http://localhost:8080/users/set-password/{id}',
                'tech.matrix.learner@gmail.com', 
                [form.cleaned_data.get('email')])
            messages.success(request, f'An email has been sent to {email}')
            return redirect('twitter-home')
    else:
        form = PasswordResetForm()
        return render(request, 'users/reset_password.html', context={'form': form})


def set_password(request, id):
    user = User.objects.get(pk=id)
    if request.method == "GET":
        form = SetPasswordForm(user=user)
        return render(request, 'users/set_password.html', context= {'form': form})
    else:
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your password has been successfully changed, you can login now.')
            return redirect('twitter-home')
        messages.error(request, f'Something went wrong, please try again activating your account.')
        return render(request, 'users/set_password.html', context= {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('twitter-home')


def view_profile(request, pk):
    pass

def update_profile(request, pk):
    pass

def delete_profile(request, pk):
    pass
    
class ProfileDetailView(DetailView):
    model = Profile
