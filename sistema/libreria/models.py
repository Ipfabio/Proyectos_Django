from django.db import models

# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField( max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen",null=True)
    descripcion = models.TextField(null=True, verbose_name="Descripción")
    
    def __str__(self):
        fila = f"Titulo: {self.titulo} - Descripción: {self.descripcion}"
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) # Para que al borrar, se elimine la imágen del Storage
        super().delete()