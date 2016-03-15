from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', lista_pessoas, name='namespace_lista_pessoas'),
    url(r'^cadastrar_pessoa/$', cadastrar_pessoa, name='namespace_cadastrar_pessoa'),
    url(r'^detalhes_pessoa/(?P<id>[0-9]+)/$', detalhes_pessoa, name='namespace_detalhes_pessoa'),
    url(r'^atualizar_pessoa/(?P<id>[0-9]+)/$', atualizar_pessoa, name='namespace_atualizar_pessoa'),
    url(r'^excluir/(?P<id>[0-9]+)/$', excluir, name='namespace_excluir'),
]