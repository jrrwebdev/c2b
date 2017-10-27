from django.conf.urls import url
from core import views

urlpatterns = (
    url(r'^anunciar/', views.anunciar, name='anunciar'),
    url(r'^sucesso/$', views.home, name='sucesso'),

    url(r'^meusanuncios/$', views.meusanuncios, name='meusanuncios'),

    url(r'^novousuario/$', views.novousuario, name='novousuario'),
    url(r'^signupvendedor/$', views.signupvendedor, name='signupvendedor'),
    url(r'^signupcomprador/$', views.signupcomprador, name='signupcomprador'),
)
