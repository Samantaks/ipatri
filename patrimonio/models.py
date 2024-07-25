from django.db import models
from usuario.models import Setor


class Contacontabil(models.Model):
    idcontacontabil = models.AutoField(primary_key=True)
    tipocontacontabil = models.CharField(max_length=50)
    durabilidade = models.CharField(max_length=11)
    item_idpatrimonio = models.ForeignKey('Item', models.DO_NOTHING, db_column='item_idpatrimonio')

    class Meta:
        managed = False
        db_table = 'contacontabil'


class Depreciacao(models.Model):
    iddepreciacao = models.AutoField(primary_key=True)
    tipodepreciacao = models.CharField(max_length=100)
    datacomprafk = models.DateField(blank=True, null=True)
    datamanutencaofk = models.DateField(blank=True, null=True)
    valordepreciado = models.DecimalField(max_digits=9, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'depreciacao'


# Create your models here.
class Item(models.Model):
    idpatrimonio = models.AutoField(primary_key=True)
    tombo = models.IntegerField(blank=True, null=True)
    itemnome = models.CharField(max_length=200, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    datacompra = models.DateField(blank=True, null=True)
    itemano = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    valorcompra = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    notafiscal = models.IntegerField(blank=True, null=True)
    depreciacao_iddepreciacao1 = models.ForeignKey(Depreciacao,
                                                   models.DO_NOTHING, db_column='depreciacao_iddepreciacao1')
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor')

    class Meta:
        managed = False
        db_table = 'item'
