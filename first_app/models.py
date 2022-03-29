from django.db import models


# Create your models here.
class Mrs(models.Model):
    project_id = models.IntegerField()
    mr_id = models.IntegerField()
