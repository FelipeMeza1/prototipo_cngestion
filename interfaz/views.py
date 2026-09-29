from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def leads(request):
    return render(request, 'core/leads.html')

def perfil_cliente(request):
    return render(request, 'core/perfil_cliente.html')