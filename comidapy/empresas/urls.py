from django.conf.urls import url
from . import views

urlpatterns = [

	# /empresas/
	url(r'^$', views.empresas, name='empresas'),

	# /empresas/detalle
	url(r'^detalle/(?P<id>[0-9]+)/$', views.detalle, name='detalle' ),
	url(r'^nuevo/$', views.nuevo, name="nuevo"),
	url(r'^eliminar/(?P<id>[0-9]+)/$', views.eliminar, name="eliminar" ),
	url(r'^editar/(?P<id>[0-9]+)/$', views.editar, name='editar' ),
]