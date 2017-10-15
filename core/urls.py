from django.conf.urls import url
from core import views

urlpatterns = (
    url(r'^customer_add', views.customer_add, name='cadastrar'),

)
