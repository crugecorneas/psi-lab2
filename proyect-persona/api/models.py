from django.db import models

class Persona(models.Model):
    """
    Modelo que representa una persona.
    """
    id = models.AutoField(primary_key=True)  # id como AutoField para generar un valor entero único automáticamente
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        Representación en cadena del modelo.
        """
        return f"{self.apellido}, {self.nombre}"
