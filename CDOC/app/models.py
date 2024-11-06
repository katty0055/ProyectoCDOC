# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#    * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import os
from django.db import models

from .utils import generate_html_documentation, parse_comments_from_file


class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_archivo = models.CharField(max_length=255)
    archivo_c = models.FileField(upload_to='archivosC/', blank=True, null=True)
    archivo_html = models.FileField(upload_to='archivosHTML/', blank=True, null=True)

    def __str__(self):
        # Mostrar el nombre del archivo_c sin la ruta
        return os.path.basename(self.archivo_c.name) if self.archivo_c else 'Sin archivo'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.archivo_c and not self.archivo_html:
            base_name = os.path.splitext(os.path.basename(self.archivo_c.name))[0]
            html_file_name = f'{base_name}.html'
            html_file_path = os.path.join('media', 'archivosHTML', html_file_name)

            comments = parse_comments_from_file(self.archivo_c.path)
            generate_html_documentation(comments, html_file_path)

            self.archivo_html.name = f'archivosHTML/{html_file_name}'
            super().save(update_fields=['archivo_html'])

    
    class Meta:
        db_table = 'archivos'