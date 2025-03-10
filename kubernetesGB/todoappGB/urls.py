from django.urls import path, include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=False), name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('add_task/', views.add_task, name='add_task')
]