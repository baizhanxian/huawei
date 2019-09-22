# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from db.base_model import BaseModel


class Third_app(BaseModel):
    app_id = models.CharField(max_length=64, null=False, verbose_name='应用AppID', unique=True)
    app_secret = models.CharField(max_length=64, null=False, verbose_name='应用App密钥')

    # app_description = models.CharField(max_length=100, verbose_name='应用App描述',blank=True)
    # type = models.IntegerField(default=0)

    class Meta:
        db_table = 'third_app'
        verbose_name = '应用App'
        verbose_name_plural = verbose_name

    @classmethod
    def validate_password(cls, app_id, app_secret):

        return cls.objects.filter(app_id=app_id, app_secret=app_secret).exists()
