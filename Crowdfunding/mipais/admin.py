from django.contrib import admin
from .models import TipoPersona, MedioPago, Estado, Persona, Proyecto, Donacion

# Register your models here.


admin.site.register(TipoPersona)
admin.site.register(MedioPago)
admin.site.register(Estado)
admin.site.register(Persona)
admin.site.register(Proyecto)
admin.site.register(Donacion)