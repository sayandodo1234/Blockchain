from django.db import models
from hashlib import sha256
import json
from django.contrib import admin

# Create your models here.

class Block(models.Model):
    #blockchain = models.ForeignKey(Blockchain, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100,editable=False)
    location = models.CharField(max_length=100,editable=False)
    buyer = models.CharField(max_length=100,editable=False)
    seller = models.CharField(max_length=100,editable=False)
    prev_hash = models.CharField(max_length=1000,default='00',editable=False)
    hash = models.CharField(max_length=1000,default='0', editable=False)

    def compute_hash(self):
        rec_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(rec_string.encode()).hexdigest()


class Blockchain(models.Model):
    #id = models.IntegerField(default=0,primary_key=True)
    #block = models.ForeignKey(Block,on_delete=models.CASCADE)
    amount = models.CharField(max_length=100,default=None,editable=False)
    location = models.CharField(max_length=100,default=None,editable=False)
    buyer = models.CharField(max_length=100,default=None,editable=False)
    seller = models.CharField(max_length=100,default=None,editable=False)
    prev_hash = models.CharField(max_length=1000,default='00',editable=False)
    hash = models.CharField(max_length=1000,default='0', editable=False)

class Node(models.Model):
    url = models.CharField(max_length=100,default=None)




