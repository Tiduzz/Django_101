from core.models import Evento
from django.contrib import admin

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'date_evento', 'date_creation')
    list_filter = ('titulo',)

admin.site.register(Evento, EventoAdmin)