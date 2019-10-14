"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required #para decorar los resultados de las url
from web.views import  IndexView, RankingView,LogView #LoginView, LogoutView,
from usuario.views import CreateUserView, LoginView, LogoutView, LoginView2


urlpatterns = [
    path('admin/', admin.site.urls),
    #Url de login y logout
    #url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),
    #url del index
    url(r'^$', IndexView.as_view(), name='web_index'),
    #Url ranking
    url(r'^ranking$', RankingView.as_view(), name='web_ranking'),
 
    url(r'^logintest$',LogView.as_view(),name='web_logintest'),
    #Urls de la app usuarios
    #Url para listar usuarios proximamente
    #Url para registrar usuario
    url(r'^user/signup$', CreateUserView.as_view(), name='user_create' ),
    path('login', LoginView2.as_view(), name='user_login'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
