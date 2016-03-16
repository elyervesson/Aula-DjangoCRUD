from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = ['primeiro_nome', 'ultimo_nome', 'email', 'idade', 'genero' , 'periodo', 'cra', 'curso']