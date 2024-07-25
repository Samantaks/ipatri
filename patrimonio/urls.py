from django.urls import path
from .views import *


urlpatterns = [
    path('novo', itemcadastro, name='item-cadastro'),
    path('visita', itemvisita, name='visita-setor'),
    path('movimentacao', itemmov, name='movimentacao'),
]
