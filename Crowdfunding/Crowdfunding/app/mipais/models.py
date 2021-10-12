from django.db import models

# Create your models here.

class TipoPersona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True, max_length = 30)

    def __str__(self):
        return self.nombre

class MedioPago(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True, max_length = 30)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(unique = True, max_length = 30)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    idtipopersona = models.ForeignKey(TipoPersona, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    documento = models.IntegerField(unique = True)
    email = models.EmailField(max_length = 50)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.usuario

class Proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    idpersona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    idestado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 50)
    progreso = models.IntegerField() #Suma de las donaciones

    def __str__(self):
        return self.nombre

class Donacion(models.Model):
    id = models.AutoField(primary_key = True)
    idpersona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    idproyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    idmediopago = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.cantidad