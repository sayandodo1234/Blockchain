from .models import Data,unconfirmeddata
from hashlib import sha256
class Block:
    def __init__(self, index,amount,location,buyer,seller, time, prev_hash="000", nonce=0):
        #constructor of block
        self.index = index
        self.Amount = amount
        self.Location = location
        self.Buyer = buyer
        self.Seller=seller
        self.timestamp = time
        self.prev_hash = prev_hash
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
            j += 1
