from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django import forms

from website.models import Funcionario

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

class FuncionarioListView(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    context_object_name = 'funcionarios'

class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None

        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:

            funcionario = Funcionario\
                .objects\
                .filter(id=id)\
                .first()

        return funcionario

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )

class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )


