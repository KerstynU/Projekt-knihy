from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models

# takhle to bude vypadat v databázi
# Create your models here.
class Kniha(models.Model):
    jmeno = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    rok = models.IntegerField()


    class Meta:
        verbose_name_plural = "Knihy"

    def __str__(self):
        return self.jmeno