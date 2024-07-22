from django.contrib import admin
from .models import Item, Depreciacao, Contacontabil

# Register your models here.
admin.site.register(Item)
admin.site.register(Depreciacao)
admin.site.register(Contacontabil)
