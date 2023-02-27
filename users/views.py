from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)



def profile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'users/single-profile.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            error_message = 'Invalid credentials. Please try again.'
    else:
        error_message = ''

    return render(request, 'users/login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('edit-account')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required(login_url='login')
def account(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
        
    context = {'form': form, }
    return render(request, 'users/edit-account.html', context)