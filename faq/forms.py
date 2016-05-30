from django import forms
from django.utils.html import escape
from django.db.models import Q
from django.utils.translation import ugettext as _


class DudasForm (forms.Form):
	nombre = forms.CharField (label = 'Nombre*', 
								max_length = 200, 
								widget=forms.TextInput(attrs={
									'size': 30,
									'placeholder': 'Introduzca aquí su nombre',
								}), 
							)

	TIPOS_DUDAS = ( ('-1', '-- Seleccione un tipo --'), ('0', 'Área comercial'), ('1', 'Área académica'), ('2', 'Registro y Control'),  ('3', 'Área financiera'), ('4', 'Área de marketing'),)
	tipo = forms.ChoiceField(label = 'Tipo de duda*', 
										choices = TIPOS_DUDAS, 
									)
										
	email = forms.EmailField(label = 'Correo electrónico*',
								widget=forms.TextInput(attrs={
									'size': 30,
									'placeholder': 'Escriba aquí su E-mail',
								}), )
	
	detalle = forms.CharField(label = 'Detalle*', 
								widget = forms.Textarea(attrs={
									'cols':30,
									'placeholder': 'Detalle aquí su duda o sugerencia',
								}))
	
	def clean(self):
		cleaned_data = super(DudasForm, self).clean()
		
		t = self.cleaned_data.get('tipo')
		
		if int(t) < 0:
			raise forms.ValidationError(_("Por favor, seleccione un tipo de duda."))
			