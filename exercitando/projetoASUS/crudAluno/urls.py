from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^lista_pessoas/$', lista_pessoas, name='namespace_lista_pessoas'),
]