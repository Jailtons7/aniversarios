from django.urls import reverse
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormMixin

from app.models import Aniversarios
from app.forms import AniversariosForm


class BirthdayCalendarView(ListView, FormMixin):
    template_name = "aniversarios/base.html"
    model = Aniversarios
    form_class = AniversariosForm

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BirthdayCalendarView, self).get_context_data(**kwargs)
        context['title'] = "Calendário de Aniversários"
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form=form)
        return self.form_invalid(form=form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(BirthdayCalendarView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse('aniversarios:aniversarios_list')


class BirthdayCalendarDelete(DeleteView):
    model = Aniversarios

    def get_success_url(self):
        return reverse('aniversarios:aniversarios_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
