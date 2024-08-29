from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name  = 'home/signup.html'
    success_url = '/smart/notes'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {"today":datetime.today()}

class AuthorizeView(LoginRequiredMixin , TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

# def home(request):
#     return render(request , 'home/welcome.html', {"today":datetime.today()})
# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request , 'home/authorize.html', {})