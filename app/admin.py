from django.contrib import admin

from .models import Aniversarios


@admin.register(Aniversarios)
class AniversariosAdmin(admin.ModelAdmin):
    list_display = ('aniversariante', 'user', 'dt_aniversario')
    list_display_links = ('aniversariante',)
    search_fields = ('aniversariante', 'user')

