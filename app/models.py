from django.db import models

# Create your models here.
class Funcionario(models.Model):
    name = models.CharField(max_length=100, null= False, blank=False)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    birthday_date = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    
