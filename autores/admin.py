from django.contrib import admin

from autores.models import Autor


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_nascimento")
    search_fields = ("nome",)
    ordering = ("nome",)

admin.site.register(Autor, AutorAdmin)