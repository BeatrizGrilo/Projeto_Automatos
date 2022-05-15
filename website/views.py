from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .desenharAFD import desenha_automato
from .desenharMT import desenha_MT
from .models import Automato, MaquinaTuring
from .forms import AutomatoForm, MaquinaTuringForm
from .validar import validar_sequencia
from .validarTM import validar_TM

from django.shortcuts import render
from website.forms import ValidarForm, ValidarTMForm

import json
import os

def introducao_page_view(request):
	return render(request, 'website/introducao.html')

def automatos_page_view(request):
    data= {'automatos': Automato.objects.all()}
    return render(request, 'website/automatos.html', data)

def maquinaturing_page_view(request):
    data = {'maquinasturing': MaquinaTuring.objects.all()}
    return render(request, 'website/maquinasturing.html', data)

def novo_automato_view(request):
    form = AutomatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoinicial = form.data.get('estadoinicial')
        estadodeaceitacao = form.data.get('estadodeaceitacao')
        transicoes = form.data.get('transicoes')
        desenha_automato(descricao, estados, estadoinicial, estadodeaceitacao, transicoes)
        return HttpResponseRedirect(reverse('website:automatos'))

    context = {'form': form}

    return render(request, 'website/novo.html', context)


def edita_automato_view(request, automato_id):
    automato = Automato.objects.get(id=automato_id)
    name = Automato.objects.get(id=automato_id).descricao
    form = AutomatoForm(request.POST or None, instance=automato)

    if form.is_valid():
        form.save()
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoinicial = form.data.get('estadoinicial')
        estadodeaceitacao = form.data.get('estadodeaceitacao')
        transicoes = form.data.get('transicoes')
        os.remove('website/static/website/images/' + name + '.svg')
        desenha_automato(descricao, estados, estadoinicial, estadodeaceitacao, transicoes)
        return HttpResponseRedirect(reverse('website:automatos'))

    context = {'form': form, 'automato_id': automato_id}
    return render(request, 'website/edita.html', context)


def apaga_automato_view(request, automato_id):
    name = Automato.objects.get(id=automato_id).descricao
    Automato.objects.get(id=automato_id).delete()
    os.remove('website/static/website/images/' + name + '.svg')
    return HttpResponseRedirect(reverse('website:automatos'))

def detalhes_page_view(request, automato_id):
    data= {'detalhes': Automato.objects.get(id=automato_id)}
    return render(request, 'website/detalhes.html', data)

def validar(request, automato_id):

    resultado = expressao = None

    if request.POST:
        form = ValidarForm(request.POST)
        if form.is_valid():
            expressao = form.cleaned_data['expressao']
            try:
                resultado = validar_sequencia(expressao,automato_id)
            except:
                resultado = "expressão inválida"

    form = ValidarForm(None)

    context = {
        'form': form,
        'resultado': resultado,
        'expressao': expressao
    }

    return render(request, 'website/validar.html', context)

def doesFileExists(file):
    return os.path.exists(file)


def uploadJSON(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        with open(name, 'r') as json_file:
            info = json.load(json_file)

        id = Automato.objects.all()[Automato.objects.all().count() - 1].id + 1
        alfabeto = info["alfabeto"]
        estados = info["estados"]
        estadoinicial = info["estadoinicial"]
        estadosdeaceitacao = info["estadosdeaceitacao"]
        transicoes = info["transicoes"]


        form = Automato(id, alfabeto, estados, estadoinicial,estadosdeaceitacao, transicoes)
        form.save()

    return render(request,'website/uploadAutomatos.html')


def nova_maquinaturing_view(request):
    form = MaquinaTuringForm(request.POST or None)
    if form.is_valid():
        form.save()
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoinicial = form.data.get('estadoinicial')
        estadodeaceitacao = form.data.get('estadodeaceitacao')
        transicoes = form.data.get('transicoes')
        desenha_MT(descricao, estados, estadoinicial, estadodeaceitacao, transicoes)
        return HttpResponseRedirect(reverse('website:maquinasturing'))

    context = {'form': form}

    return render(request, 'website/novoTM.html', context)


def edita_maquinaturing_view(request, turing_id):
    maquinaturing = MaquinaTuring.objects.get(id=turing_id)
    name = MaquinaTuring.objects.get(id=turing_id).descricao
    form = MaquinaTuringForm(request.POST or None, instance=maquinaturing)

    if form.is_valid():
        form.save()
        descricao = form.data.get('descricao')
        estados = form.data.get('estados')
        estadoinicial = form.data.get('estadoinicial')
        estadodeaceitacao = form.data.get('estadodeaceitacao')
        transicoes = form.data.get('transicoes')
        os.remove('website/static/website/imagesMT/'+ name +'.svg')
        desenha_MT(descricao, estados, estadoinicial, estadodeaceitacao, transicoes)
        return HttpResponseRedirect(reverse('website:maquinasturing'))

    context = {'form': form, 'turing_id': turing_id}
    return render(request, 'website/editaTM.html', context)


def apaga_maquinaturing_view(request, turing_id):
    name = MaquinaTuring.objects.get(id=turing_id).descricao
    MaquinaTuring.objects.get(id=turing_id).delete()
    os.remove('website/static/website/imagesMT/' + name + '.svg')
    return HttpResponseRedirect(reverse('website:maquinasturing'))

def detalhes_maquinaturing_view(request, turing_id):
    data= {'detalhesTM': MaquinaTuring.objects.get(id=turing_id)}
    return render(request, 'website/detalhesTM.html', data)

def uploadJSON_TM(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        with open(name, 'r') as json_file:
            info = json.load(json_file)

        id = MaquinaTuring.objects.all()[MaquinaTuring.objects.all().count() - 1].id + 1
        alfabeto = info["alfabeto"]
        estados = info["estados"]
        estadoinicial = info["estadoinicial"]
        estadofinal = info["estadofinal"]
        estadosdeaceitacao = info["estadosdeaceitacao"]
        transicoes = info["transicoes"]


        form = MaquinaTuring(id, alfabeto, estados, estadoinicial, estadofinal, estadosdeaceitacao, transicoes)
        form.save()

    return render(request,'website/uploadTM.html')

def validarTM(request, turing_id):

    resultado = expressao = None

    if request.POST:
        form = ValidarTMForm(request.POST)

        if form.is_valid():

            expressao = form.cleaned_data['expressao']
            try:
                resultado = validar_TM(expressao, turing_id)
            except:
                resultado = "expressão inválida"

    form = ValidarTMForm(None)

    context = {
        'form': form,
        'resultado': resultado,
        'expressao': expressao
    }

    return render(request, 'website/validarTM.html', context)




