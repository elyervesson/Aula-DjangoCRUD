from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
		fields = ['primeiro_nome', 'ultimo_nome', 'email', 'idade', 'genero' , 'periodo', 'cra', 'curso']