# coding=utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings

from faq.models import FuentesJSON
from faq.forms import *

import urllib.request
import json


def index(request):
	if request.method == 'POST':
		dudas_form = DudasForm(request.POST)

		if dudas_form.is_valid():
			nom = escape(dudas_form.cleaned_data['nombre'])
			tip = int(dudas_form.cleaned_data['tipo'])
			mail = escape(dudas_form.cleaned_data['email'])
			det = escape(dudas_form.cleaned_data['detalle'])
			
			# Enviar notificación
			TIPOS_DUDAS = ( ('-1', '-- Seleccione un tipo --'), ('0', 'Área comercial'), ('1', 'Área académica'), ('2', 'Registro y Control'),  ('3', 'Área financiera'), ('4', 'Área de marketing'), ('5', 'Otras cuestiones'))
			path = request.build_absolute_uri(reverse('faq:index'))
			mensj = "Se ha recibido una nueva duda desde " + path +".\n\nNombre: " + nom + "\nCorreo electrónico: " + mail + "\nDetalle: " + det
			email_dest = 'tecnologia.ns@iep.edu.es'

			send_mail('Formación CRM - Duda de ' + TIPOS_DUDAS[tip+1][1], mensj, settings.DEFAULT_FROM_EMAIL, [email_dest], fail_silently=False)
			
			return render(request, 'faq/redirect.html')
			
		else:
			return render(request, 'faq/index.html', { 'dudas_form': dudas_form })
			
	else:   # GET
		dudas_form = DudasForm()
		fuente = get_object_or_404(FuentesJSON, nombre = "faq")

		response = urllib.request.urlopen(fuente.filename_fuente)
		preguntas = json.loads(response.read().decode('utf-8'))

		context = {
				'dudas_form': dudas_form,
				'preguntas': preguntas
		}
		
		return render(request, 'faq/index.html', context)
