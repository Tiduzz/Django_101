from django.http import response
from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {'eventos' : evento}
    return render(request, 'agenda.html', dados)

def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválidos")
    return redirect('/')

@login_required(login_url='/login')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        date_evento = request.POST.get('date_evento')
        description = request.POST.get('description')
        usuario = request.user
        local = request.POST.get('local')
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.date_evento = date_evento
                evento.description = description
                evento.local = local
                evento.save()
        else:
            Evento.objects.create(titulo=titulo,
                                date_evento=date_evento, 
                                description=description,
                                local=local,
                                usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')