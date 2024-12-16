from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm, InicioSesionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    return render(request, 'home.html')

def salir(request):
    logout(request)
    return redirect('/')

def registro(request):
    data = {
        'form':RegistroForm()
    }

    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['email'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has registrado con exito!.')
            return redirect (home)
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)