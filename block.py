import hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.hash = hashlib.sha256()
        self.prev_hash = prev_hash
        self.nonce = 0
        self.data = data

    def __str__(self):
        return "{prev_hash}{data}{increment}".format( prev_hash = self.prev_hash.hexdigest(), data = self.data, increment = self.nonce)
    
    def minecraft(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        
        # the point of the difficulty is to limit the range of hashes to a smaller one, this makes it harder to guess with a hash function for which a cap cannot be enforced
        while int(self.hash.hexdigest(), 16) >= 2 ** (256 - difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8')) # recall that a single change causes the entire sha256 algo to produce a completely new output, thus this method
        
        #!! DISABLE TO NOT PRINT THE ORIGIN NODE 
        #for display purposes
        #hey u know it works since it printed a crap ton when it was accidentally put in the while loop lol
        #print("\n------------------------------")
        #print(f"Hash: {self.hash.hexdigest()}")
        #print(f"Prev Hash: {self.prev_hash.hexdigest()}")
        #print(f"Nonce: {self.nonce}")
        #print(f"Data: {self.data}")
        #print("------------------------------\n")

    