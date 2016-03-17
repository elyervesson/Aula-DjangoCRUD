from django.shortcuts import render, redirect

# Create your views here.
from .models import Aluno
from .forms import AlunoForm

def lista_alunos(request):
	alunos = Aluno.objects.all()
	context = {
		"alunos": alunos
	}
	return render(request, 'lista_alunos.html', context)

def cadastrar_aluno(request):
	form = AlunoForm(request.POST or None)
	if form.is_valid():
		aluno = Aluno()
		aluno = form.save(commit=False)
		aluno.save()
		return redirect('namespace_lista_alunos')
	context = {
		'form' : form
	}
	return render(request, 'cadastrar_aluno.html', context)

def detalhes_aluno(request, id):
	aluno = Aluno.objects.get(pk=id)
	context = {
		'aluno':aluno
	}
	return render(request, 'detalhes_aluno.html', context)

def atualizar_aluno(request, id):
	aluno = Aluno.objects.get(pk=id)
	form = AlunoForm(request.POST or None, instance=aluno)
	if form.is_valid():
		aluno = form.save(commit=False)
		aluno.save()
		return redirect('namespace_lista_alunos')
	context = {
		'form':form
	}
	return render(request, 'cadastrar_aluno.html', context)
	
def excluir_aluno(request, id):
	aluno = Aluno.objects.get(pk=id)
	aluno.delete()
	return redirect('namespace_lista_alunos')