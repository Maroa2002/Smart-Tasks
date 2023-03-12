from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/smart/tasks'
    template_name = 'home/signup.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/home_page.html'

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'home/home_page.html'
    extra_context = {'today': datetime.today}

