from django.views.generic import ListView, CreateView

from app.models import Aniversarios
from app.forms import AniversariosForm


class BirthdayCalendarView(ListView):
    template_name = "aniversarios/base.html"
    model = Aniversarios

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BirthdayCalendarView, self).get_context_data(**kwargs)
        context['aniversario_form'] = AniversariosForm()
        return context
