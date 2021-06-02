# Testing for main

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from main import Transaction, Block, Chain, Wallet
from bottom import to_bottom, from_bottom

bottom_penguin = Chain()

# unit tests
def unit_tests():
    test_tran = Transaction(1500, to_bottom("genesis"), to_bottom("pinguin0"))

    print(test_tran.get_string())

    # assert test_tran.get_string() == '{"amount": 1500, "payer": "\ud83d\udc96\ud83d\udc96,,,\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96,\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\u2728\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96,\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\u2728\ud83e\udd7a\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\ud83e\udd7a\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\u2728\ud83e\udd7a\ud83d\udc49\ud83d\udc48", "payee": "\ud83d\udc96\ud83d\udc96\u2728,,\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\ud83e\udd7a\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\u2728\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96,,,\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\u2728\ud83e\udd7a,,\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\ud83e\udd7a\ud83d\udc49\ud83d\udc48\ud83d\udc96\ud83d\udc96\u2728\ud83d\udc49\ud83d\udc48\u2728\u2728\u2728\u2728\ud83e\udd7a,,,\ud83d\udc49\ud83d\udc48"}', "Transaction error"

    test_block = Block(None, test_tran)

    print(test_block.get_hash())

    bottom_text = "💖💖,,,👉👈💖💖,👉👈💖💖✨👉👈💖💖,👉👈💖💖✨🥺👉👈💖💖🥺👉👈💖💖✨🥺👉👈"
    print(to_bottom("genesis"))

    assert bottom_text == to_bottom("genesis"), "invalid bottom"

# actual runs
def blockchain_test():
    penguin0 = Wallet()
    penguin1 = Wallet()
    penguin2 = Wallet()

    penguin0.send(bottom_penguin, 50, penguin1.get_public_key())
    penguin1.send(bottom_penguin, 23, penguin2.get_public_key())
    penguin2.send(bottom_penguin, 5, penguin1.get_public_key())

    print(bottom_penguin.get_last_block())

unit_tests()
blockchain_test()
