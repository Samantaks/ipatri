from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboardpage, name='app-home'),
    path('retorna_total_gasto', retorna_total_gasto, name='app-retorna-total-gasto'),
    path('relatorio_gasto', relatorio_gasto, name='app-relatorio-gasto'),
    path('relatorio_marcas', relatorio_marcas, name='app-relatorio-marcas'),
]