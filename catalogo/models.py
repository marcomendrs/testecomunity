from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        null=False
    )
    modified_at=models.DateTimeField(
        auto_now=True,
        null=False
    )
    active=models.BooleanField(
        default=True
    )

    class Meta:
        abstract=True


class State(ModelBase):
    name= models.CharField(
        null=False,
        max_length=64
    )
    abbreviation=models.CharField(
        max_length=2,
        null=False
    )
    def __str__(self):
        return self.name
    class Meta:
        db_table='state'
        managed=True

class City(ModelBase):
    name=models.CharField(
        null=False,
        max_length=64

    )
    state=models.ForeignKey(
        to=State,
        on_delete=models.DO_NOTHING,
        db_column='id_state',

    )
    def __str__(self):
        return self.name
    class Meta:
        db_table='city'
        managed=True
class Modelo(ModelBase):
    class MaritalStatus(models.TextChoices):
        S = ('SOLTEIRA', 'Solteira')
        N = ( 'NAMORANDO', 'Namorando')
        C = ('CASADA', 'Casada')

    name= models.CharField(
        null=False,
        max_length=64
    )
    city=models.ForeignKey(
        to=City,
        on_delete=models.DO_NOTHING,
        db_column='id_city'
    )

    username= models.CharField(
        null=False,
        max_length=64
    )
    age= models.IntegerField(
        null=False,

    )
    height = models.FloatField(
        null=False

    )
    child = models.BooleanField(
        default=False
    )
    marital_status = models.CharField(
        null=False,
        max_length=64,
        default=False,
        choices= MaritalStatus.choices
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table='modelo'
        managed=True