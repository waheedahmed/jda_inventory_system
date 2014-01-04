from django.contrib.auth.models import User
from django.db import models


class Equipment(models.Model):
  tag = models.CharField(max_length=100, null=False, unique=True)
  description = models.TextField(max_length=500, null=True)
  location = models.TextField(max_length=500, null=True)
  created_at = models.DateTimeField(auto_now_add=True)


class Currency(models.Model):
  name = models.CharField(max_length=50, null=False)
  code = models.CharField(max_length=10, null=False)
  user = models.ForeignKey(User, editable=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.name

class Part(models.Model):
  equipment = models.ForeignKey(Equipment, null=False)
  code = models.CharField(max_length=100, null=False, unique=True)
  part_number = models.CharField(max_length=100, null=False, unique=True)
  quantity = models.IntegerField(null=False)
  max_level = models.IntegerField(null=False)
  min_level = models.IntegerField(null=False)
  reorder_point = models.IntegerField(null=False)
  description = models.TextField(max_length=500, null=True)
  location = models.TextField(max_length=500, null=True)
  vendor_detail = models.TextField(max_length=500, null=True)
  last_price = models.DecimalField(null=False, decimal_places=2, max_digits=20)
  currency = models.ForeignKey(Currency, null=False)
  issued_by = models.ForeignKey(User, null=True)
  issued_to = models.CharField(max_length=100, null=True)
  issued_date = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)


class PartLog(models.Model):
  part = models.ForeignKey(Part, null=False)
  description = models.TextField(max_length=500, null=True)
  location = models.TextField(max_length=500, null=True)
  quantity = models.IntegerField(null=False)
  issued_by = models.ForeignKey(User, null=False)
  issued_to = models.CharField(max_length=100, null=False)
  issued_date = models.DateTimeField(null=False)
  created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
  user = models.ForeignKey(User, null=False)
  message = models.CharField(max_length=100, null=True)
