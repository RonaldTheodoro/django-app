from django.db import models


class Person(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf', max_length=11, blank=True, null=True)
    email = models.EmailField('email', unique=True)
    birth_date = models.DateField('data de nascimento')

    def __str__(self):
        return self.name
