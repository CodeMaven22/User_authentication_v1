from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.conf import settings


def home(request):
    return render(request, 'UserAccounts/home.html')


def login_view(request):
    form = LoginForm()  # Instantiate the form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend='UserAccounts.authentication_backends.CustomUserAuthBackend')
                # Redirect based on role
                if user.role == 'student':
                    return redirect('students_portal')
                elif user.role == 'lecturer':
                    return redirect('lecturers_dashboard')
                elif user.role == 'registrar':
                    return redirect('registrar_dashboard')
            else:
                return HttpResponse("Invalid login credentials.")
    return render(request, 'UserAccounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='UserAccounts.authentication_backends.CustomUserAuthBackend')

            # Redirect based on role after registration
            if user.role == 'student':
                return redirect('students_portal')
            elif user.role == 'lecturer':
                return redirect('lecturers_dashboard')
            elif user.role == 'registrar':
                return redirect('registrar_dashboard')
            else:
                return redirect('home')  # Default redirection if no specific role
    else:
        form = RegistrationForm()
    return render(request, 'UserAccounts/register.html', {'form': form})