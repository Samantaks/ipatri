from django.db import models
from usuario.models import Setor, Usuario


class Alocacao(models.Model):
    idalocacao = models.AutoField(primary_key=True)
    dataalocacao = models.DateTimeField(blank=True, null=True)
    estado_idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_idestado')
    item_idpatrimonio = models.ForeignKey('Item', models.DO_NOTHING, db_column='item_idpatrimonio',
                                          verbose_name='usuario', related_name='Alocacao')
    user = models.ForeignKey(Usuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'alocacao'


class Contacontabil(models.Model):
    idcontacontabil = models.AutoField(primary_key=True)
    nomecc = models.CharField(max_length=100, blank=True, null=True)
    descricaocc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nomecc}'

    class Meta:
        managed = False
        db_table = 'contacontabil'


class Depreciacao(models.Model):
    iddepreciacao = models.AutoField(primary_key=True)
    nometipodepreciacao = models.CharField(max_length=200, blank=True, null=True)
    vidautil = models.IntegerField(blank=True, null=True)
    taxaanual = models.IntegerField(blank=True, null=True)
    contacontabil_idcontacontabil = models.ForeignKey(Contacontabil,
                                                      models.DO_NOTHING, db_column='contacontabil_idcontacontabil')

    def __str__(self):
        return f' {self.nometipodepreciacao} para {self.contacontabil_idcontacontabil}'

    class Meta:
        managed = False
        db_table = 'depreciacao'


class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True)
    tipoestado = models.CharField(max_length=45)
    descricaoestado = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.tipoestado}'

    class Meta:
        managed = False
        db_table = 'estado'


class Item(models.Model):
    idpatrimonio = models.AutoField(primary_key=True)
    itemnome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tombo = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    itemano = models.IntegerField(blank=True, null=True)
    datacompra = models.DateField(blank=True, null=True)
    valorcompra = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    notafiscal = models.IntegerField(blank=True, null=True)
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado_idestado')
    depreciacao_iddepreciacao1 = models.ForeignKey(Depreciacao, models.DO_NOTHING,
                                                   db_column='depreciacao_iddepreciacao1', blank=True, null=True)
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor', blank=True, null=True)
    contacontabil_idcontacontabil = models.ForeignKey(Contacontabil, models.DO_NOTHING,
                                                      db_column='contacontabil_idcontacontabil', blank=True, null=True)

    def __str__(self):
        return f'{self.idpatrimonio} - {self.itemnome}:  {self.setor_id_setor}'

    class Meta:
        managed = False
        db_table = 'item'


class Visita(models.Model):
    idvisita = models.AutoField(primary_key=True)
    datavisita = models.DateField(blank=True, null=True)
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor')
    tombos_visita = models.TextField(blank=True, null=True)
    visita_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='visita_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visita'
