from django import forms
from .models import Archivos
# from .models import Archivos
# Integrantes

# Aldo Sebastian Medina Ozorio
# Ana Paula Gonzalez Alvariza
# Katteryne Alice Gaona Alcaraz


class ArchivosForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ['archivo_c']
