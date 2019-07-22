# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    cname=models.CharField(max_length=20,unique=True,verbose_name='类别名称')

    class Meta:
        db_table='t_category'
        verbose_name_plural='类别'

    def __unicode__(self):
        return u'%s'%self.cname



class Tags(models.Model):
    tname=models.CharField(max_length=20,unique=True)

    class Meta:
        db_table='t_tags'
        verbose_name_plural = '标签'

    def __unicode__(self):
        return u'%s'%self.tname


class Post(models.Model):
    title=models.CharField(max_length=100,unique=True)
    desc=models.TextField()
    content=RichTextField(config_name='mycfg')
    created=models.DateField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tags)

    class Meta:
        db_table='t_post'
        verbose_name_plural = '帖子'


    def __unicode__(self):
        return u'%s'%self.title


