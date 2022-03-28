from django.db import models


# Create your models here.
class FirstObj(models.Model):
    column_num = models.IntegerField()
    column_char = models.CharField(max_length=30)
