from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', lista_alunos, name='namespace_lista_alunos'),
    url(r'^cadastrar_aluno/$', cadastrar_aluno, name='namespace_cadastrar_aluno'),
    url(r'^detalhes_aluno/(?P<id>[0-9]+)/$', detalhes_aluno, name='namespace_detalhes_aluno'),
    url(r'^atualizar_aluno/(?P<id>[0-9]+)/$', atualizar_aluno, name='namespace_atualizar_aluno'),
    url(r'^excluir_aluno/(?P<id>[0-9]+)/$', excluir_aluno, name='namespace_excluir_aluno'),
]