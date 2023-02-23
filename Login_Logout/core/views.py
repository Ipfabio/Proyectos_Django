from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Con esto generamos la necesidad de logearme para poder ingresar a una vista (Se aplica como un decorador)
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return  render(request, 'core/home.html')

@login_required
def products(request):
    return render(request, 'core/products.html')


def exit(request):
    logout(request)
    return redirect('home')