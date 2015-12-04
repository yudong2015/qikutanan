#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User,related_name='person')
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)

#class Rewards(models.Model):   #奖池
#    name = models.CharField(max_length=50)
#    amount = models.IntegerField()
#    remain = models.IntegerField()

class Reward(models.Model):  #奖励
    type = models.CharField(u'奖励类型',max_length=50)
    number = models.CharField(u'奖券号',unique=True,max_length=20)
    password = models.CharField(u'奖券密码',max_length=20)
    remain = models.IntegerField(u'剩余奖券总数')

class DrawRecord(models.Model):  #抽奖记录
    user = models.OneToOneField(User, related_name='draw')
    reward = models.ForeignKey(Reward,related_name='draw')
    created_time = models.DateTimeField(auto_now_add=True)
