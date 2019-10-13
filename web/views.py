from django.http import HttpResponse
from django.http import response
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.
class LoginView(View):
    def get(self, request):
        template_name = 'usuario/login.html'
        context = {}
        return render(request,template_name,context)

class LogoutView(View):
    def get(self, request):
        template_name = 'principal.html'
        context = {}
        return render(request,template_name,context)

# index del proyecto
class IndexView(View):
    def get(self,request):
        template_name = 'principal.html'
        context = {}
        return render(request, template_name, context)

# index del proyecto
class RankingView(View):
    def get(self, request):
        template_name = 'ranking.html'
        context = {}
        return render(request, template_name, context)

# index del login
class LogView(View):
    def get(self, request):
        template_name = 'logintest.html'
        context = {}
        return render(request, template_name, context)
