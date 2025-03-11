from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import TodoItem, Priority
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Rediriger vers la page d'accueil après la connexion
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    users = User.objects.all()
    tasks = TodoItem.objects.all()
    return render(request, 'home.html', {'users': users, 'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task-name')
        description = request.POST.get('task-desc')
        user_item = request.user
        priority_value = request.POST.get('priority')
        
        # Convertir la valeur de priorité en objet Priority
        priority = None
        if priority_value == 'low':
            priority = Priority.objects.get(name='Low')
        elif priority_value == 'medium':
            priority = Priority.objects.get(name='Medium')
        elif priority_value == 'high':
            priority = Priority.objects.get(name='High')
        
        TodoItem.objects.create(
            title=title,
            description=description,
            UserItem=user_item,
            priority=priority
        )
        return redirect('home')
    return redirect('home')
