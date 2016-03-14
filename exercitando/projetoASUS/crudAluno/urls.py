from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', lista_pessoas, name='namespace_lista_pessoas'),
    url(r'^cadastrar_pessoa/', cadastrar_pessoa, name='namespace_cadastrar_pessoa'),
]