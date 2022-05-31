from django.contrib import admin
from core.models import Evento
# Register your models here.

#criando uma lista personalizada
class EventonAdmin(admin.ModelAdmin):
     list_display = ('titulo','dataEvento','dataCriacao','usuario')
     list_filter = ('usuario','dataEvento')

admin.site.register(Evento,EventonAdmin)
