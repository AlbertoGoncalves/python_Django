from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.


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
            messages.error(request, "Usuario ou sennha invalida")

    return redirect('/')



@login_required(login_url='/login/')
def lista_eventos(request):
    # Como consultar um dado da tabela
    # evento = Evento.objects.get(id=1)
    # .all para trazer todos os Registros
    usuario = request.user

    data_atual = datetime.now() - timedelta(hours=1)

    # Validando registros por usuarios Filter
    evento = Evento.objects.filter(usuario=usuario,
                                   dataEvento__gt=data_atual)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)




@login_required(login_url='/login/')
def json_lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)


@login_required(login_url='/login/')
def json_lista1_eventos(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)





@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    print(id_evento)
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        desc_evento = request.POST.get('desc_evento')
        usuario = request.user
        id_evento = request.POST.get('id_evento')

        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.dataEvento = data_evento
                evento.descricao = desc_evento
                evento.save()

            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                      dataEvento=data_evento,
            #                      descricao=desc_evento,
            #                      usuario=usuario)
        else:
            Evento.objects.create(titulo=titulo,
                                  dataEvento=data_evento,
                                  descricao=desc_evento,
                                  usuario=usuario)

    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()

    return redirect('/')