from autores.models import Autor
from django import forms
from django.utils.translation import gettext_lazy as _


class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nome", "biografia", "data_nascimento"]
        widgets = {
            "data_nascimento": forms.DateInput(
                attrs={
                    "placeholder": _("Data de nascimento"),
                    "data-input": "data-input",
                    "type": "date"
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance is not None:
            self.initial['data_nascimento'] = instance.data_nascimento.strftime('%Y-%m-%d') # noqa
