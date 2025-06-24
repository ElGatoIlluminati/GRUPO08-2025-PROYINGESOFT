from django.shortcuts import render

# Create your views here.

def home_view(request):
    """
    Esta vista se encarga de renderizar la página de inicio.
    """
    return render(request, 'home.html')