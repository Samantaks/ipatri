from django.db import models


class Setor(models.Model):
    id_setor = models.AutoField(primary_key=True)
    setor_abrev = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    orgao_full = models.CharField(max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)
    setor_full = models.CharField(max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)
    orgao_abrev = models.CharField(max_length=15, db_collation='utf8mb3_general_ci', blank=True, null=True)
    responsavel_setor = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.setor_abrev} - {self.orgao_abrev} | {self.responsavel_setor}"

    class Meta:
        managed = False
        db_table = 'setor'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nomeusuario = models.CharField(max_length=150, blank=True, null=True)
    sobrenome = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    senha = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(db_column='CPF', max_length=15, blank=True, null=True)
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor',
                                       verbose_name='Setor', related_name='usuarios')

    def __str__(self):
        return f'{self.cpf} - {self.nomeusuario} {self.sobrenome}'

    class Meta:
        managed = False
        db_table = 'usuario'
