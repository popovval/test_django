from django.db import models


# Create your models here.
class Change(models.Model):
    owner = models.CharField(verbose_name="OWNER NAME", max_length=128)
    is_merged = models.BooleanField(verbose_name='IS MERGED', default=False)
    is_deleted = models.BooleanField(verbose_name='IS DELETED', default=False)
    created_ts = models.DateTimeField(verbose_name='CREATED AT', auto_now_add=True)
    updated_ts = models.DateTimeField(verbose_name='UPDATED AT', auto_now=True)
    uniq_source_change_id = models.CharField(verbose_name="SOURCE CHANGE ID", max_length=128, default='')
