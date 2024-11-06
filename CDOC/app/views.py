# app/views.py

import os
from django.conf import settings
from django.shortcuts import render, redirect

from .utils import generate_html_documentation, parse_comments_from_file
from .forms import ArchivosForm

def cargar_archivo(request):
    if request.method == 'POST':
        form = ArchivosForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save() 
            return redirect('listar_archivos')
    else:
        form = ArchivosForm()
    return render(request, 'archivos/cargar_archivo.html', {'form': form})


def listar_archivos(request):
    from .models import Archivos  # Mover la importación aquí
    archivos = Archivos.objects.all()
    return render(request, 'archivos/lista_archivos.html', {'archivos': archivos})
