from django.urls import path

from DjangoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('contacto', views.contact, name="Contacto"),
    path('servicios', views.services, name="Servicios"),
    path('blog', views.blog, name="Blog"),
    path('tienda', views.store, name="Tienda"),
]
