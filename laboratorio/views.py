from django.shortcuts import render, redirect, HttpResponse
from .forms import LaboratorioForm
from .models import Laboratorio
# Create your views here.

def insertar_lab(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mostrar/')
    form = LaboratorioForm()
    context = {'form':form}
    return render(request, 'laboratorio/insertar.html', context)

def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    num_visitas = request.session.get('num_visitas', 1)
    request.session['num_visits'] = num_visitas+1
    context = {
        'laboratorios': laboratorios,
        'num_visitas': num_visitas
    }

    return render(request, 'laboratorio/mostrar.html', context)