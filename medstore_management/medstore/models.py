from django.db import models

# Create your models here.
class Dealer(models.Model):
    dname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    sal = models.CharField(max_length=20)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email

class Customer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email

class Medicine(models.Model):
    m_name = models.CharField(max_length=30)  
    dname = models.CharField(max_length=30)
    price = models.IntegerField()
    mrp = models.IntegerField()

    def __str__(self):
        return self.m_name
                