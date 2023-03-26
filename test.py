# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:48:01 2023

"""

from cq import CircularQueue

cq = CircularQueue()
print("Starting Size", len(cq) )
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
print("Current Size", len(cq) )
print("Current Head", cq.first())
cq.rotate()
print("Current Head after rotating", cq.first())


print("-"*60)

print("Testing adding from the front and back as well as dequeue")

print("-"*60)

cq2 = CircularQueue()
cq2.enqueue("10")
cq2.enqueue("20")
cq2.enqueue("30")

cq2.add_to_front("40")
cq2.add_to_front("50")
cq2.add_to_front("60")

cq2.dequeue()

cq2.traverse()