from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, UpdateView

from app.models import Aniversarios
from app.forms import AniversariosForm


class BirthdayCalendarView(LoginRequiredMixin, ListView, FormMixin):
    template_name = "aniversarios/base.html"
    login_url = reverse_lazy('login')
    redirect_field_name = 'ir_para'
    model = Aniversarios
    form_class = AniversariosForm

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

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


class BirthdayCalendarDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'ir_para'
    model = Aniversarios

    def get_success_url(self):
        return reverse('aniversarios:aniversarios_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class BirthdayCalendarEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'ir_para'
    model = Aniversarios
    fields = ('aniversariante', 'dt_aniversario')

    def get_success_url(self):
        return reverse('aniversarios:aniversarios_list')
