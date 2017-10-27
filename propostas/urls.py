from django.conf.urls import url
from propostas.views import new, detail

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^([\w-]+)/', detail, name='detail'),
]