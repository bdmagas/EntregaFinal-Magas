from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import RegistroUsuarioForm, EditarPerfilForm, EditarProfileExtendidoForm
from .models import Perfil

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    # después de registrarse, va a login
    else:
        form = RegistroUsuarioForm()
    
    contexto = {'form': form}
    return render(request, 'accounts/registration/register.html', contexto)


@login_required
def perfil_usuario(request):
    contexto = {'user': request.user}
    return render(request, 'accounts/profile.html', contexto)

@login_required
def editar_perfil(request):
    usuario = request.user

    try:
        perfil = usuario.perfil
    except ObjectDoesNotExist:
        perfil = Perfil.objects.create(user=usuario)

    if request.method == 'POST':
        form_user = EditarPerfilForm(request.POST, instance=usuario)
        form_profile = EditarProfileExtendidoForm(request.POST, request.FILES, instance=perfil)

        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            return redirect('perfil')
    else:
        form_user = EditarPerfilForm(instance=usuario)
        form_profile = EditarProfileExtendidoForm(instance=perfil)

    contexto = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    return render(request, 'accounts/edit_profile.html', contexto)
