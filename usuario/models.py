from django.db import models


class Setor(models.Model):
    id_setor = models.AutoField(primary_key=True)
    setor_abrev = models.CharField(max_length=250, db_collation='utf8mb3_general_ci')
    orgao_full = models.CharField(max_length=250, db_collation='utf8mb3_general_ci')
    setor_full = models.CharField(max_length=250, db_collation='utf8mb3_general_ci')
    orgao_abrev = models.CharField(max_length=250, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'setor'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nomeusuario = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=50)
    role = models.CharField(max_length=1)
    cpf = models.IntegerField(db_column='CPF')  # Field name made lowercase.
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor')

    class Meta:
        managed = False
        db_table = 'usuario'