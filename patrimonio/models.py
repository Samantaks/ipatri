from django.db import models
from usuario.models import Setor


class Contacontabil(models.Model):
    idcontacontabil = models.AutoField(primary_key=True)
    nomecc = models.CharField(max_length=100, blank=True, null=True)
    descricaocc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacontabil'


class Depreciacao(models.Model):
    iddepreciacao = models.AutoField(primary_key=True)
    nometipodepreciacao = models.CharField(max_length=200, blank=True, null=True)
    valordepreciado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    natureza = models.CharField(max_length=100, blank=True, null=True)
    contacontabil_idcontacontabil = models.ForeignKey(Contacontabil,
                                                      models.DO_NOTHING, db_column='contacontabil_idcontacontabil')

    class Meta:
        managed = False
        db_table = 'depreciacao'


# Create your models here.
class Item(models.Model):
    idpatrimonio = models.AutoField(primary_key=True)
    itemnome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tombo = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    itemano = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    datacompra = models.DateField(blank=True, null=True)
    valorcompra = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    notafiscal = models.IntegerField(blank=True, null=True)
    depreciacao_iddepreciacao1 = models.ForeignKey(Depreciacao, models.DO_NOTHING,
                                                   db_column='depreciacao_iddepreciacao1')
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor')

    def __str__(self):
        return f'{self.idpatrimonio} - {self.itemnome}:  {self.setor_id_setor}'

    class Meta:
        managed = False
        db_table = 'item'
