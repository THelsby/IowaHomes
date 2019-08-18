from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    """ Allows user to sign up if the passwords match and the username is no already in the system

    Parameters:
    request (request): holds the information about the web page.

    Returns:
    render : django shortcut to allow you to pass request data, html page and data.

   """
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')


def login(request):
    """ Allows user to log in if they have an account in the database

    Parameters:
    request (request): holds the information about the web page.

    Returns:
    render : django shortcut to allow you to pass request data, html page and data.

   """
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


# TODO need to route to home page and dont forget to logout
def logout(request):
    """ Allows user to log out if they're currently logged in

    Parameters:
    request (request): holds the information about the web page.

    Returns:
    render : django shortcut to allow you to pass request data, html page and data.

   """
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/signup.html')
