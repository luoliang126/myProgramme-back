from django.db import models

class User(models.Model):
    # 用户名称
    username = models.CharField(max_length=20)

    # 联系电话
    mobile = models.CharField(max_length=11)

    # 密码
    password = models.CharField(max_length=18)
