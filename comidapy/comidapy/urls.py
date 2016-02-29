from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
    
    # view de app
	url(r'^$', views.user_login, name='user_login'),
    url(r'^index/$', views.index, name='index'),

    # Otros modulos
    url(r'^admin/', admin.site.urls),
    url(r'^empresas/', include('empresas.urls')),
    
]
