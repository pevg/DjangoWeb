from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, "DjangoWebApp/home.html")

def blog(request):
   return render(request, "DjangoWebApp/blog.html")

def services(request):
   return render(request, "DjangoWebApp/services.html")

def store(request):
   return render(request, "DjangoWebApp/store.html")

def contact(request):
   return render(request, "DjangoWebApp/contact.html")