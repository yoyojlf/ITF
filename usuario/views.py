from django.http import HttpResponse
from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q
from usuario.models import Usuario
from usuario.forms import UsuarioForm, LoginForm
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

# Create your views here.
#Login y logout
class LoginView(View):
    def get(self,request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request,'usuario/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd', '')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    """
                                        if user.is_superuser:
                        url = request.GET.get('next', 'admin')
                        return redirect(url)
                    elif user.is_staff:
                        return redirect('admin')
                    else:
                        return redirect('index')
                    """
                    url = request.GET.get('next', 'web_index')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request,'usuario/login.html', context)

#Prueba de login cargado con formulario en html
class LoginView2(View):
    def get(self,request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request,'usuario/logintest.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd', '')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    """
                                        if user.is_superuser:
                        url = request.GET.get('next', 'admin')
                        return redirect(url)
                    elif user.is_staff:
                        return redirect('admin')
                    else:
                        return redirect('index')
                    """
                    url = request.GET.get('next', 'web_index')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request,'usuario/login.html', context)

class LogoutView(View):
    @method_decorator(login_required())
    def get(self,request):
        if request.user.is_authenticated:
            django_logout(request)
        return redirect('web_index')



# Vista de crear usuario
class CreateUserView(View):

    #@method_decorator(login_required())
    def get(self,request):
        """
        esto cmuestra un formulario para registrar un usuario
        :param request:
        :return:
        """
        form = UsuarioForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'usuario/new_user.html', context)

    #@method_decorator(login_required())
    def post(self,request):
        """
        esto cmuestra un formulario para crear una foto y la crea
        :param request:
        :return:
        """

        success_message = ''

        form = UsuarioForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #form = PhotoForm()
            success_message = 'Usuario guardado con éxito'
        else:
            success_message = 'Informacion no valida'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'usuario/new_user.html', context)

class ProfileView(View):
    @method_decorator(login_required())
    def get(self,request):

        return render(request, 'Perfil.html')

class EvaView(View):
    @method_decorator(login_required())
    def get(self,request):

        return render(request, 'Evaluaciones.html')
