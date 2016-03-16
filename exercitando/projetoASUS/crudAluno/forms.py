from django import forms
from .models import Estudante

class EstudanteForm(forms.ModelForm):
	class Meta:
		model = Estudante
		fields = ['primeiro_nome', 'ultimo_nome', 'email', 'idade', 'genero' , 'periodo', 'cra', 'curso']