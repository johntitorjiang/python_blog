#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from xadmin import views
from .models import Article, Aboutme


class BaseSetting(object):
    enable_themes = True
    use_boots_watch = True


class GlobalSettings(object):
    site_title = "Jiang_Ginger_Blog"
    site_footer = "Jiang_Ginger"
    # menu_style = "accordion"


class ArticleAdmin(object):
    list_display = ["title", "category", "content", "add_time"]
    search_fields = ["title", "category", "content", "add_time"]
    list_filter = ["title", "category", "content", "add_time"]
    style_fields = {"content": "ueditor"}


class AboutmeAdmin(object):
    list_display = ["content", "add_time"]
    search_fields = ["content", "add_time"]
    list_filter = ["content", "add_time"]
    style_fields = {"content": "ueditor"}


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Aboutme, AboutmeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
