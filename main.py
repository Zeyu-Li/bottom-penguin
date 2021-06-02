'''
Bottom Penguin
Synergize the scalable Quantum Machine Learn Blockchain technology to the moon serverlessly 🥺👉👈
'''

import random
from bottom import to_bottom, from_bottom # from the dependency (installed with `python3 setup.py install`)
from datetime import datetime
import hashlib
import json


class Transaction:
    """
    An individual transaction in the blockchain
    """
    def __init__(self, amount: float, payer: str, payee: str):
        self.amount = amount
        self.payer = payer
        self.payee = payee
    
    def get_string(self) -> str:
        current_transaction = dict()
        current_transaction["amount"] = self.amount
        current_transaction["payer"] = self.payer
        current_transaction["payee"] = self.payee

        return json.dumps(current_transaction)

class Block:
    """
    A block in the blockchain
    """
    def __init__(self, previous_hash: str, transaction: Transaction):
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.now = datetime.now()

    def get_hash(self):
        block_string = json.dumps({
            "previous_hash": self.previous_hash,
            "transaction": self.transaction.get_string(),
            "now": str((self.now-datetime(1970,1,1)).total_seconds()),
        })
        # inits hash
        current_hash = hashlib.sha256()
        current_hash.update(block_string.encode('utf-8'))

        return current_hash.hexdigest()


class Chain:
    """
    Start of the blockchain and the blockchain itself
    """
    def __init__(self):
        genesis_block = Block(None, Transaction(1500, to_bottom("genesis"), to_bottom("pinguin0")))
        self.chain = [genesis_block]

    def get_last_block(self) -> Block:
        return self.chain[len(self.chain) - 1]

    def add_block(self, transaction: Transaction, sender_public_key: str, signature) -> None:
        new_block = Block(self.get_last_block().get_hash(), transaction)
        self.chain.append(new_block)

class Wallet:
    def __init__(self, public_key: str, private_key: str):
        self.public_key = public_key
        self.private_key = private_key

    def get_public_key(self) -> str:
        return self.public_key
