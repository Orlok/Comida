from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


from .forms import EmpresaForm
from .models import Empresa


# @login_required
def empresas(request):
	empresas = Empresa.objects.all()
	template = 'empresas.html'
	contexto = {
		'empresas': empresas
	}
	return render(request,template, contexto)

@login_required
def detalle(request, id ):
	# empresa = Empresa.objects.get(pk=id) 
	empresa = get_object_or_404(Empresa, pk=id)
	template = 'empresa_detalle.html'
	contexto = {
		'empresa': empresa
	}
	return render(request,template, contexto)


@login_required
def nuevo(request):
	if request.method == "POST":
		formulario = EmpresaForm(request.POST)
		if formulario.is_valid():
			empresa = formulario.save(commit=False)
			empresa.createdby = request.user
			empresa.save()
			send_mail("Alta de Empresa", 
					  "Se dio de alta la empresa X",
					  '"origen" <notificaciones@nuvoil.com>',
					  ['carlos.martinez@nuvoil.com'])
			return HttpResponseRedirect("/empresas/")
	else:
		formulario = EmpresaForm()

	template = 'empresa_nueva.html' 
	contexto = {
		'formulario': formulario
	}
	return render(request,template,contexto)
	# return render_to_response(template, contexto)
	# return render_to_response(template,
	# 							context_intance = RequestContext(request, contexto)
	# 							)


@login_required
def eliminar(request, id):
	empresa = get_object_or_404(Empresa, pk=id)
	empresa.delete()
	return HttpResponseRedirect("/empresas/")


@login_required
def editar(request, id):
	empresa = get_object_or_404(Empresa, pk=id)

	if request.method == "POST":
		formulario = EmpresaForm(request.POST, instance=empresa)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/empresas/")
	else:
		formulario = EmpresaForm(instance=empresa)

	template= 'empresa_editar.html'
	contexto = {
		'formulario': formulario		
	}
	return render(request, template, contexto)

