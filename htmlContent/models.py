from django.db import models

class htmlContent(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 内容
    content = models.CharField(max_length=10000)

# 将User表添加注册到admin管理界面，就可以实现admin管理这张表
from django.contrib import admin
admin.site.register(htmlContent)
