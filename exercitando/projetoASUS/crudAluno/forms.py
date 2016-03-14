from django import forms
from .models import Pessoa, Aluno

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = ['primeiro_nome', 'ultimo_nome', 'email', 'idade', 'genero']

class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
		fields = ['periodo', 'cra']