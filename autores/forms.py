from django.forms import ModelForm

from autores.models import Autor


class AutorForms(ModelForm):
    class Meta:
        model = Autor
        fields = ("nome", "biografia", "data_nascimento")