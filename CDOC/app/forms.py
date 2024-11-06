from django import forms
from .models import Archivos
# from .models import Archivos

class ArchivosForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ['archivo_c']
