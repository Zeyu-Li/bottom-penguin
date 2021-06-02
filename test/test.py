import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from main import Transaction, Block, Chain, Wallet
from bottom import to_bottom, from_bottom

bottom_penguin = Chain()

# unit tests
def unit_test():
    test_tran = Transaction(1500, to_bottom("genesis"), to_bottom("pinguin0"))

    print(test_tran.get_string())

    test_block = Block(None, test_tran)

    print(test_block.get_hash())

    print(to_bottom("genesis"))

# actual runs
def blockchain_test():
    penguin0 = Wallet()
    penguin1 = Wallet()
    penguin2 = Wallet()

    penguin0.send(bottom_penguin, 50, penguin1.get_public_key())
    # penguin1.send(23, penguin2.get_public_key())
    # penguin2.send(5, penguin1.get_public_key())

blockchain_test()
