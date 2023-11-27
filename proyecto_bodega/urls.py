"""
URL configuration for proyecto_bodega project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from proyecto_bodega.views import saludar_con_html,acerca_de_mi

# Estas son las URLS generales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path("productos-ventas/",include("productos_ventas.urls")),
    path("inicio/",saludar_con_html, name="inicio"),
    path("perfiles/", include("perfiles.urls")),
    path("acerca-de-mi/",acerca_de_mi, name="acerca_de_mi"),
]
# Agregamos esto al final, para incluir los archivos media: imagenes, etc
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)