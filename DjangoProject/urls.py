"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from livraria.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro_list/', livro_list, name='livro_list'),
    path('livro_new/', livro_new, name='livro_new'),
    path('livro_edit/<int:pk>', livro_edit, name='livro_edit'),
    path('livro_delete/<int:pk>', livro_remove, name='livro_remove')
]
