"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from cars.views import NewCarCreateView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view


# onde ficam todas as rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'), #name é o nome da view
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # serve para configurar o Django para servir arquivos de mídia (uploads de usuários, por exemplo) durante o desenvolvimento.
# static() é usada para anexar uma rota específica para servir arquivos estáticos (como imagens, documentos) 
# settings.MEDIA_URL: Define a URL base para acessar os arquivos de mídia.
# settings.MEDIA_ROOT: Define o diretório no sistema de arquivos onde os arquivos de mídia são armazenados.