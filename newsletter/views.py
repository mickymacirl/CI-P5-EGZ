from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import SignUp

def newsletter(request):
    return render(request, 'newsletter/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'newsletter/index.html', {'form': form})
