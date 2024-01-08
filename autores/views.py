from autores import forms, models
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class AutorListView(generic.ListView):
    model = models.Autor
    context_object_name = "autores"
    template_name = "autores/autor_list.html"
    paginate_by = 5


class AutorCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = models.Autor
    form_class = forms.AutorForms
    template_name = "autores/autor_form.html"
    success_url = reverse_lazy("autores:list")
    success_message = "Autor criado com sucesso!"


class AutorUpdateView(views.SuccessMessageMixin, generic.UpdateView):
    model = models.Autor
    form_class = forms.AutorForms
    template_name = "autores/autor_form.html"
    success_url = reverse_lazy("autores:list")
    success_message = "Autor atualizado com sucesso!"


class AutorDeleteView(views.SuccessMessageMixin, generic.DeleteView):
    model = models.Autor
    template_name = "autores/autor_confirm_delete.html"
    success_url = reverse_lazy("autores:list")
    success_message = "Autor excluído com sucesso!"


class AutorDetailView(generic.DetailView):
    model = models.Autor
    context_object_name = "autor"
    template_name = "autores/autor_detail.html"
