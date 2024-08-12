from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboardpage, name='app-home'),
    path('estoque', estoque, name='app-estoque'),
    path('localizacao', localizacao, name='app-localizacao'),
    path('retorna_total_gasto', retorna_total_gasto, name='app-retorna-total-gasto'),
    path('retorna-quantidade-setores/', retorna_quantidade_setores, name='app-retorna-quantidade-setores'),
    path('relatorio_gasto', relatorio_gasto, name='app-relatorio-gasto'),
    path('relatorio_marcas', relatorio_marcas, name='app-relatorio-marcas'),
    path('relatorio_setor', relatorio_setor, name='app-relatorio-setor'),
    path('export_estoque_xls/', export_estoque_xls, name='export_estoque_xls'),
]