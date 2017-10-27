from django.conf.urls import url, include
from core import views
from propostas import views as prop


urlpatterns = (
    url(r'^anunciar/', views.anunciar, name='anunciar'),
    url(r'^sucesso/$', views.home, name='sucesso'),

    url(r'^meusanuncios/$', views.meusanuncios, name='meusanuncios'),
    url(r'^minhaspropostas/$', views.minhaspropostas, name='minhaspropostas'),

    url(r'^propostas/', include('propostas.urls')),


    url(r'^novousuario/$', views.novousuario, name='novousuario'),
    url(r'^signupvendedor/$', views.signupvendedor, name='signupvendedor'),
    url(r'^signupcomprador/$', views.signupcomprador, name='signupcomprador'),
)
