# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023

"""

class CircularQueue:
    """Queue implementation using circularly linked list for storage"""
    
    # Create an inner class 'Node' that represents a single node in the linked list we use to implement a Circular Queue
    class _Node:       
        def __init__(self, element, next_node=None):
            self._element = element
            self._next = next_node
    
    # Attributes of the CircularQueue class are defined
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    # Method len returns the current size of the queue
    def __len__(self):
        return self._size
    
    # Method returns True if queue is empty and False otherwise
    def is_empty(self):
        return self._size == 0
    
    # Method returns the element that is currently at the head of the queue. Raises an exception if the queue is empty
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element
    
    # Method removes the node at the head of the queue (allowing for exceptions such as an empty queue)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        element = self._head._element
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
            self._tail._next = self._head
        self._size -= 1
        return element

    # Method adds an element to the back of the queue.
    def enqueue(self, element):
        new_node = self._Node(element)
        # If the queue is empty, it sets both head and tail to the new node.
        if self.is_empty():
            new_node._next = new_node
            self._head = new_node
            self._tail = new_node
        else:
        # Otherwise, it sets the next attribute of the new node to the current head
            new_node._next = self._tail._next
        # Sets the next attribute of the current tail node to the new node
            self._tail._next = new_node
        # Sets tail to the new node
            self._tail = new_node
        # Finally it increases queue size by 1
        self._size += 1

    # Method transfers the item at the head of the list to the tail of the list
    def rotate(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self._tail = self._head
        self._head = self._head._next
       
    # Bonus Method! add an element from the front    
    def add_to_front(self, element):
        new_node = self._Node(element)
        # If the queue is empty, it sets both head and tail to the new node.
        if self.is_empty():
            new_node._next = new_node
            self._head = new_node
            self._tail = new_node
        else:
            # Otherwise, it sets the next attribute of the new node to the current head
            new_node._next = self._head
            # Sets the head to the new node
            self._head = new_node
            # Sets the next attribute of the current tail node to the new node
            self._tail._next = self._head
        # Finally, it increases queue size by 1
        self._size += 1

    # Bonus Method! Traverse
    def traverse(self):
        # define the first node
        curr_node = self._head
        
        # as long as there is a next node keep going
        while curr_node._next:
            
            # print the data
            print(curr_node._element)
            curr_node = curr_node._next
            
            if curr_node == self._head:
                break