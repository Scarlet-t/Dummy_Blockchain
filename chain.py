import hashlib
from block import Block
class Chain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []
        self.create_origin()

    def __str__(self):
        pnt = ""
        for i in range(0, len(self.blocks)):
            pnt += "\n{num}------------------------------\n".format(num = i + 1)
            pnt += "Hash: {hash}\nPrev Hash: {prev_hash}\nNonce: {nonce}Data: {data}\n".format(hash = self.blocks[i].hash.hexdigest(), prev_hash = self.blocks[i].prev_hash.hexdigest(), nonce = self.blocks[i].nonce, data = self.blocks[i].data)
        return pnt

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        # ensures that it is hashed properly and that it meets the difficulty requirements 
        # also ensures that the previous hash in the block is the same as the previous hash in this object's block list
        # changing the hash of one block requires changing the blocks that follow it as the hash of each previous one is stored in each block
        # we often have multiple machines hashing the blocks, and we assume that the majority of them are not tampering with the blocks, so if one of them provides a block with a hash that's not the same as the others, we know it's been tampered with
        # and even so, it probably wouldn't pass the first condition of this return (unless the proof of work is tampered with)
        return {block.hash.hexdigest() == hash.hexdigest() 
                and int(hash.hexdigest(), 16) < 2**(256 - self.difficulty)
                and block.prev_hash == self.blocks[-1].hash
                }
    
    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self, data):
        self.pool.append(data)

    def create_origin(self):
        prev_hash = hashlib.sha256()
        prev_hash.update(' '.encode('utf-8'))
        origin = Block("mimu", prev_hash)
        origin.minecraft(self.difficulty)
        self.blocks.append(origin)

    def minecraft(self):
        if len(self.pool) > 0:
            data = self.pool.pop() #take first piece of data
            block = Block(data, self.blocks[-1].hash)
            block.minecraft(self.difficulty)
            self.add_to_chain(block)
        print("\n------------------------------")
        print(f"Hash: {block.hash.hexdigest()}")
        print(f"Prev Hash: {block.prev_hash.hexdigest()}")
        print(f"Nonce: {block.nonce}")
        print(f"Data: {block.data}")
        print("------------------------------\n")