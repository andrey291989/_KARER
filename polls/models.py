from django.db import models

cat = (('Белаз','Белаз'), ('Kamatsu','Kamatsu'))

# Create your models here.
class Samosval(models.Model):
    nomer = models.CharField(unique = True, max_length = 150)
    model = models.CharField(choices = cat, max_length = 150)
    podemnost = models.IntegerField(default = 1)
    zagrujennost = models.IntegerField(default = 7)
    zapolnen = models.IntegerField(blank = True)

   # def __str__(self):
    #    """Возвращает строковое представление модели."""
    #    return self.nomer, self.model

