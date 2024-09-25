from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Bienvenido a tu pagina")  # retorna en la pagina home
    return render(request, 'myapp/home.html')
def about(request):
    #return HttpResponse("Acerca de esta pagina")# retorna en una pagina acerca de 
    return render(request, 'myapp/about.html')
def contact(request):
    #return HttpResponse("Pagina de Contacto") # retorna en pagina de contacto
    return render(request, 'myapp/contact.html')
def services(request):
    #return HttpResponse("Pagina de Servicios") # retorna en servicios
    return render(request, 'myapp/services.html')
def blog(request):
    #return HttpResponse("Pagina del Blog") # retorna en una blog
    return render(request, 'myapp/blog.html')

