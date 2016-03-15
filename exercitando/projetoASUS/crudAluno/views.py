from django.shortcuts import render, redirect

# Create your views here.
from .models import Pessoa, Aluno
from .forms import PessoaForm, AlunoForm

def lista_pessoas(request):
	pessoas = Pessoa.objects.all()
	context = {
		"pessoas":pessoas
	}
	return render(request, 'lista_pessoas.html', context)

def cadastrar_pessoa(request):
	form = PessoaForm(request.POST or None)
	if form.is_valid():
		pessoa = Pessoa()
		pessoa = form.save(commit=False)
		pessoa.save()
	context = {
		'form' : form
	}
	return render(request, 'cadastrar_pessoa.html', context)

def detalhes_pessoa(request, id):
	pessoa = Pessoa.objects.get(pk=id)
	context = {
		'pessoa':pessoa
	}
	return render(request, 'detalhes_pessoa.html', context)

def atualizar_pessoa(request, id):
	pessoa = Pessoa.objects.get(pk=id)
	form = PessoaForm(request.POST or None, instance=pessoa)
	if form.is_valid():
		pessoa = form.save(commit=False)
		pessoa.save()
		return redirect('namespace_lista_pessoas')
	context = {
		'form':form
	}
	return render(request, 'cadastrar_pessoa.html', context)
	
def excluir(request, id):
	pessoa = Pessoa.objects.get(pk=id)
	pessoa.delete()
	return redirect('namespace_lista_pessoas')