# encoding: utf-8
from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"博客标题")
    category = models.CharField(max_length=50, blank=False, null=False, verbose_name=u'博客标签')
    content = UEditorField(verbose_name=u"正文", imagePath="images/", width=800, height=300,
                              filePath="files/", default='')
    abstract = models.CharField(max_length=1000,default=None, blank=False, null=False, verbose_name=u"博客摘要")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']


class Aboutme(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Aboutme")
    content = UEditorField(verbose_name=u"正文", imagePath="images/", width=800, height=300,
                              filePath="files/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Aboutme"
        verbose_name_plural = verbose_name