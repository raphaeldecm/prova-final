from django.contrib.messages import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from autores import forms, models


# Create your views here.
class AutorListView(generic.ListView):
    model = models.Autor
    context_object_name = "autores"
    template_name = "autores/autor_list.html"

class AutorCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = models.Autor
    form_class = forms.AutorForms
    template_name = "autores/autor_form.html"
    success_url = reverse_lazy("autores:index")
    success_message = "Autor criado com sucesso!"

class AutorUpdateView(views.SuccessMessageMixin, generic.UpdateView):
    model = models.Autor
    form_class = forms.AutorForms
    template_name = "autores/autor_form.html"
    success_url = reverse_lazy("autores:index")
    success_message = "Autor atualizado com sucesso!"

class AutorDeleteView(views.SuccessMessageMixin, generic.DeleteView):
    model = models.Autor
    template_name = "autores/autor_confirm_delete.html"
    success_url = reverse_lazy("autores:index")
    success_message = "Autor excluído com sucesso!"

class AutorDetailView(generic.DetailView):
    model = models.Autor
    context_object_name = "autor"
    template_name = "autores/autor_detail.html" 