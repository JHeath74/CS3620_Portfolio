from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .Forms import RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def registration(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!  You are logged in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/Register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'user/profile.html')