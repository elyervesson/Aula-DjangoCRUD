from django.shortcuts import render

# Create your views here.
from .models import Pessoa, Aluno
from .forms import PessoaForm, AlunoForm

def lista_pessoas(request):
	pessoas = Pessoa.objects.all()
	context = {
		"pessoas":pessoas
	}
	return render(request, 'lista_pessoas.html', context)