from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext



from empresas.models import Empresa
from platillos.models import Platillo
from .forms import LoginForms


def index(request):

	template = 'index.html'
	contexto = {}

	return render(request, template, contexto)


def user_login(request):

	estado = None

	if request.method == 'POST':

		formulario = LoginForms(request.POST)

		if formulario.is_valid():

			usr = request.POST['usuario']
			passs = request.POST['contrasena']

			user = authenticate(username=usr, password=passs)

			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect("/index/")
				else:
					estado = "Tu cuenta no esta activa"
			else:
				estado = "Tu usuario y contrasena son incorrectas"
	else:
		formulario = LoginForms()

	template = 'login.html'
	contexto = {

		'formulario': formulario,
		'estado' : estado

	}
	return render(request, template, contexto)

