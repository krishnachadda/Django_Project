from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ExamForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        error_message = 'Invalid username or password.'

    return render(request, 'registration/login.html', {'error_message': error_message})


@login_required
def dashboard(request):
    return render(request, 'portal/dashboard.html')


@login_required
def fill_exam_form(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam form submitted successfully.')
            return redirect('dashboard')
    else:
        form = ExamForm()

    return render(request, 'portal/exam_form.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')