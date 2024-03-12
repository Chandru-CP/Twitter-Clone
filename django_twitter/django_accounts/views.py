from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('login')  # Replace 'home' with your desired redirect URL
    else:
        form = SignupForm()
    return render(request, 'django_accounts/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                # Redirect to a page after successful login
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid credentials. Please try again.')
    else:
        form = SigninForm()
    return render(request, 'django_accounts/login.html', {'form': form})


@login_required()
def dashboard(request):
    return render(request, 'django_accounts/dashboard.html')


@login_required
def sign_out(request):
    logout(request)
    return redirect('login')

