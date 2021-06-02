import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from main import Transaction, Block, Chain, Wallet
from bottom import to_bottom, from_bottom

# unit tests
test_tran = Transaction(1500, to_bottom("genesis"), to_bottom("pinguin0"))

print(test_tran.get_string())

test_block = Block(None, test_tran)

print(test_block.get_hash())

print(to_bottom("genesis"))

# actual runs

