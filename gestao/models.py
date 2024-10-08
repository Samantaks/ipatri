# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alocacao(models.Model):
    idalocacao = models.AutoField(primary_key=True)
    dataalocacao = models.DateField(blank=True, null=True)
    item_idpatrimonio = models.ForeignKey('Item', models.DO_NOTHING, db_column='item_idpatrimonio')
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    estado_idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_idestado')

    class Meta:
        managed = False
        db_table = 'alocacao'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    vidautil = models.IntegerField(blank=True, null=True)
    taxaanual = models.IntegerField(blank=True, null=True)
    contacontabil_idcontacontabil = models.ForeignKey(Contacontabil, models.DO_NOTHING, db_column='contacontabil_idcontacontabil')

    class Meta:
        managed = False
        db_table = 'depreciacao'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True)
    tipoestado = models.CharField(max_length=45)
    descricaoestado = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Item(models.Model):
    idpatrimonio = models.AutoField(primary_key=True)
    itemnome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tombo = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    itemano = models.TextField(blank=True, null=True)  # This field type is a guess.
    datacompra = models.DateField(blank=True, null=True)
    valorcompra = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    notafiscal = models.IntegerField(blank=True, null=True)
    estado_idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado_idestado')
    depreciacao_iddepreciacao1 = models.ForeignKey(Depreciacao, models.DO_NOTHING, db_column='depreciacao_iddepreciacao1')
    setor_id_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='setor_id_setor')
    contacontabil_idcontacontabil = models.ForeignKey(Contacontabil, models.DO_NOTHING, db_column='contacontabil_idcontacontabil')

    class Meta:
        managed = False
        db_table = 'item'


class Setor(models.Model):
    id_setor = models.AutoField(primary_key=True)
    orgao_full = models.CharField(max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)
    orgao_abrev = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    setor_full = models.CharField(max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)
    setor_abrev = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setor'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nomeusuario = models.CharField(max_length=150, blank=True, null=True)
    sobrenome = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    senha = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(db_column='CPF', max_length=15, blank=True, null=True)  # Field name made lowercase.
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor')

    class Meta:
        managed = False
        db_table = 'usuario'


class Visita(models.Model):
    idvisita = models.IntegerField(primary_key=True)
    datavisita = models.DateField(blank=True, null=True)
    tombos_visita = models.TextField(blank=True, null=True)
    setor_id_setor = models.ForeignKey(Setor, models.DO_NOTHING, db_column='setor_id_setor')
    visita_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='visita_usuario')

    class Meta:
        managed = False
        db_table = 'visita'
