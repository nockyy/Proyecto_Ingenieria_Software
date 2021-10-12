from django import forms
from .models import TipoPersona, MedioPago, Estado, Persona, Proyecto, Donacion

class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = '__all__'

class MedioPagoForm(forms.ModelForm):
    class Meta:
        model = MedioPago
        fields = '__all__'

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = '__all__'

