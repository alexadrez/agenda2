from django.shortcuts import render, redirect
from core.models import Evento
#from django.db import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    # evento = Evento.objects.all()
    # dados = {'eventos':evento}
    # return (request, 'agenda.html',dados)
    usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
