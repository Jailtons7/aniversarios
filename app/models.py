from django.db import models

from authentication.models import CustomUser


class Aniversarios(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    aniversariante = models.CharField(max_length=255)
    dt_aniversario = models.DateField(verbose_name="Data de Aniversário")

    class Meta:
        verbose_name = "Aniversários"
        verbose_name_plural = "Aniversários"

    def __str__(self):
        return f"{self.aniversariante}"

    def get_date(self):
        return self.dt_aniversario.strftime('%Y-%m-%d')
