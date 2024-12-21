from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Funcionario

# Create your views here.
#**************************************************
#           The Create Method
#*************************************************
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = "lista_funcionarios"
    
#****************************************************
#           The Read Method
#****************************************************
class FuncionarioListView(ListView): 
    model = Funcionario 
    template_name = "lista_funcionarios.html"
#***********************************************
#           The Update Method
#***********************************************
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ("nome", "cpf", "email", "remuneracao")
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")
#*****************************************************
#      The Detail that makes all of difference!
#*****************************************************
class FuncionarioDetailView(DetailView): 
    model = Funcionario 
    template_name = "lista_funcionario.html" 
    context_object_name = "fun"
#***************************************************
#         The Delete Method
#***************************************************
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

