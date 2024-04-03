from django.contrib import admin
from .models import Empresa, Tecnologias, Vagas


admin.site.register(Vagas)
admin.site.register(Empresa)
admin.site.register(Tecnologias)
