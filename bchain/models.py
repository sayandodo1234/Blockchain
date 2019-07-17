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

'''@admin.register(Block)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    ...
    readonly_fields = ["amount", "location", "buyer","seller","prev_hash","hash"]'''


'''class BChain(models.Model):
    block = models.ForeignKey(Block,on_delete=models.CASCADE)'''



'''class Data(models.Model):
    Amount=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Buyer=models.CharField(max_length=100)
    Seller=models.CharField(max_length=100)

    # def __str__(self):
    #     return str(self.Amount)

class unconfirmeddata(models.Model):
    data=models.ForeignKey(Data,on_delete=models.CASCADE

    def lastentry(self):
        return self.chain[-1]

    def fetch(self):
        #function to fetch from the form
        if not self.unconfirmedamount:
            return False
        if not self.unconfirmedlocation:
            return False
        if not self.unconfirmedbuyer:
            return False
        if not self.unconfirmedseller:
            return False
        #d2=Data()
        self.adddata(d2)

    def adddata(self,d1):
        self.chain.append(d1)'''

#uchain=unconfirmeddata()

'''class Block:
    def __init__(self, index,amount,location,buyer,seller, time, prev_hash="000", nonce=0):
        #constructor of block
        self.index = index
        self.Amount = amount
        self.Location = location
        self.Buyer = buyer
        self.Seller=seller
        self.timestamp = time
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.hash = self.computehash()

    def computehash(self):
        #computes the hash of block
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()



class Blockchain:
    difficulty=3

    def __init__(self):
        #constructor of blockchain
        self.chain = []
        self.unconfirmed_amount = []
        self.unconfirmed_location = []
        self.unconfirmed_buyer = []
        self.unconfirmed_seller = []

    def last_block(self):
        #Returns the last block of chain
        return self.chain[-1]

    def proof_of_work(self, block):
        #Do the proof of work of block whenever  mining is called for a block
        if len(self.chain) == 0:
            #if chain is empty
            block.index = 1
            block.prev_hash = "000"
            block.nonce = 0
            computed_hash = block.computehash()
            block.hash = computed_hash
            while not computed_hash.startswith('0' * Blockchain.difficulty):
                block.nonce += 1
                block.hash = block.computehash()
                computed_hash = block.computehash()
            return computed_hash

        block.nonce = 0
        lastblock = self.last_block()
        block.prev_hash = lastblock.hash

        computed_hash = block.computehash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            #if not hash does not start with two zeroes it will keep on varying the value of nonce
            block.nonce += 1
            computed_hash = block.computehash()
            block.hash = block.computehash()

        return computed_hash

    def mine(self):
        #Do the mining of block
        if not self.unconfirmed_amount:
            return False
        if not self.unconfirmed_location:
            return False
        if not self.unconfirmed_seller:
            return False
        if not self.unconfirmed_buyer:
            return False
        if len(self.chain) == 0:
            #if chain is empty
            new_block = Block(1, self.unconfirmed_amount, self.unconfirmed_location,
                              self.unconfirmed_buyer,self.unconfirmed_seller, time.ctime(),"000", 0)
            proof = self.proof_of_work(new_block)
            self.add_block(new_block, proof)
            return new_block.index
        else:
            lastblock = self.last_block()
            new_block = Block(lastblock.index + 1, self.unconfirmed_amount, self.unconfirmed_location,self.unconfirmed_buyer,
                              self.unconfirmed_seller,time.ctime(), lastblock.computehash(), 0)
            proof = self.proof_of_work(new_block)
            self.add_block(new_block, proof)

        return new_block.index

    def add_block(self, block, proof):
        #block is added to chain after mining
        if len(self.chain) == 0:
            #if chain is empty and first block is added
            block.hash = proof
            self.chain.append(block)
            return True
        block.hash = proof
        self.chain.append(block)
        return True

    def showdata(self):
        #prints the data of each block in the chain
        j = 1
        lastblock = self.last_block()
        m = lastblock.index
        for i in range(m, 0, -1):
            temp = self.chain[-j]
            temp.printdata()
            j += 1'''





