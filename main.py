'''
Bottom Penguin
Synergize the scalable Quantum Machine Learn Blockchain technology to the moon serverlessly 🥺👉👈
'''

import random

from rsa.key import PrivateKey, PublicKey
from bottom import to_bottom, from_bottom # from the dependency (installed with `python3 setup.py install`)
from datetime import datetime
import hashlib
import json
import rsa


class Transaction:
    """
    An individual transaction in the blockchain
    """
    def __init__(self, amount: float, payer: str, payee: str):
        self.amount = amount
        self.payer = payer
        self.payee = payee
    
    def get_string(self) -> str:
        current_transaction = {
            "amount": self.amount,
            "payer": self.payer,
            "payee": self.payee
        }

        return json.dumps(current_transaction)

class Block:
    """
    A block in the blockchain
    """

    def __init__(self, previous_hash: str, transaction: Transaction):
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.now = datetime.now()
        self.nonce = random.randint(0, 1000000000)

    def get_hash(self):
        block_string = json.dumps({
            "previous_hash": self.previous_hash,
            "transaction": self.transaction.get_string(),
            "now": str((self.now-datetime(1970,1,1)).total_seconds()),
        })
        # inits hash
        current_hash = hashlib.sha256()
        current_hash.update(block_string.encode())

        return current_hash.hexdigest()

    def get_nonce(self) -> int:
        return self.nonce


class Chain:
    """
    Start of the blockchain and the blockchain itself
    """
    def __init__(self):
        genesis_block = Block(None, Transaction(1500, to_bottom("genesis"), to_bottom("pinguin0")))
        self.chain = [genesis_block]

    def get_last_block(self) -> Block:
        return self.chain[len(self.chain) - 1]

    def mine(self, nonce: int):
        solution = 0
        print("Mining ⛏")
        while True:
            current_hash = hashlib.sha256()
            current_hash.update(str(nonce + solution).encode())

            attempt = current_hash.hexdigest()
            
            # if start with 4 0s then we are done
            if (attempt[:4] == "0000"):
                print(f"Solved with solution of {solution}")
                return solution

            solution += 1

    def add_block(self, transaction: Transaction, sender_public_key: PublicKey, signature: bytes) -> None:
        is_valid = False

        try:
            # check if valid transaction
            rsa.verify(transaction.get_string().encode(), signature, sender_public_key)
            is_valid = True
        except Exception:
            pass

        if is_valid:
            new_block = Block(self.get_last_block().get_hash(), transaction)
            self.mine(new_block.get_nonce())
            # send for validation
            self.chain.append(new_block)
        else:
            print("❌ Failed validation")

class Wallet:
    """
    Personal wallet
    """

    def __init__(self, pool_size = 1):
        size = 2048
        (self.public_key, self.private_key) = rsa.newkeys(size) # can change pool size later if need be

    def get_public_key(self) -> str:
        return str(hex(self.public_key.n))[2:] # remove hex indicator 

    def send(self, chain: Chain, amount: float, payee_public_key: str):
        transaction = Transaction(amount, self.get_public_key(), payee_public_key)

        signature = rsa.sign(transaction.get_string().encode(), self.private_key, "SHA-256")
        chain.add_block(transaction, self.public_key, signature)
