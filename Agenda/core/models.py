from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_evento = models.DateTimeField(verbose_name="Data do Evento")
    date_creation = models.DateTimeField(auto_now=True, verbose_name="Data de Criação")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'evento'
    
    def __str__(self):
        return self.titulo

    def get_date_evento(self):
        return self.date_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_date_input_evento(self):
        return self.date_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.date_evento < datetime.now():
            return True
        else:
            return False