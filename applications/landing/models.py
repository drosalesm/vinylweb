from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import model_to_dict
from embed_video.fields import EmbedVideoField


TRACK_CHOICES=(
    ('0','Cancion'),
    ('1','Beat'),    
    ('2','Instrumental'),
)


class nav_bar_opt(models.Model):
    descripcion = models.CharField(max_length=100,verbose_name="Descripcion")
    link_contenido = models.CharField(max_length=100,verbose_name="Palabra Link de contenido",null=True,blank=True)    
    posicion = models.IntegerField(verbose_name="Posicion en navegador")


    def __str__(self):
        return self.descripcion

class tracks(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    descripcion= models.CharField(max_length=500,verbose_name="Descripcion")
    tipo= models.CharField(max_length=500,verbose_name="Tipo",choices=TRACK_CHOICES)
    lanzamiento = models.DateField(null=True)
    #imagen = models.ImageField(null=True,blank=True,verbose_name="Imagen")
    #pista = models.FileField(null=True)
    pista= EmbedVideoField(null=True,blank=True)
    def __str__(self):
        return self.nombre

class en_vivo(models.Model):
    titulo = models.CharField(max_length=100,verbose_name="Descripcion")
    descripcion= models.CharField(max_length=500,verbose_name="Descripcion")
    fecha_grabacion=models.DateField(null=True,blank=True)    
    url= EmbedVideoField()

    def __str__(self):
        return self.nombre
    
class contacto(models.Model):
    telefono = models.IntegerField(verbose_name="Numero Celular")    
    correo= models.EmailField(verbose_name="Correo Electronico")
    facebook= models.CharField(max_length=500,verbose_name="Facebook")
    instagram= models.CharField(max_length=500,verbose_name="Instagram")
    youtube= models.CharField(max_length=500,verbose_name="Youtube")
    whatsapp = models.CharField(max_length=500,verbose_name="Whatsapp",null=True,blank=True)
    Direccion= models.CharField(max_length=500,verbose_name="Youtube")
    def __str__(self):
        return self.telefono

class biografia(models.Model):
    titulo = models.CharField(max_length=100,verbose_name="Titulo",null=True,blank=True)
    desc_princ= models.CharField(max_length=500,verbose_name="descripcion principal",null=True,blank=True)
    integrante_uno = models.CharField(max_length=100,verbose_name="Integrante 1",null=True,blank=True)
    integrante_dos = models.CharField(max_length=100,verbose_name="Integrante 2",null=True,blank=True)
    desc_prim= models.CharField(max_length=500,verbose_name="descripcion integrante 1",null=True,blank=True)
    desc_seg= models.CharField(max_length=500,verbose_name="descripcion integrante 2",null=True,blank=True)
    imagen_one= models.ImageField(null=True,blank=True,verbose_name="Imagen 1")
    imagen_two= models.ImageField(null=True,blank=True,verbose_name="Imagen 2")    
    imagen_three= models.ImageField(null=True,blank=True,verbose_name="Imagen 3")        
 
    def __str__(self):
        return self.titulo
