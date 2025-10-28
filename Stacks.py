import ctypes

"""Stacks using LINKEDLIST!!"""
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.top.data

    def pop(self,value):
        if self.is_empty():
            return "Stack is empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def traverse(self):

        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)
    result = ""
    while not s.is_empty():
        result = result + s.pop(text)
    return result

def text_editor(text, pattern):
    u=Stack()
    r=Stack()

    for i in text:
        u.push(i)

    for i in pattern:
        if i == "u":
            data=u.pop(text)
            r.push(data)
        else:
            data=r.pop(text)
            r.push(data)

    result = ""

    while not u.is_empty():
        result = u.pop(text) + result

        return result

"""Stacks using ARRAYS!!"""

class stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top+=1
            self.stack[self.top] = value
            return None


    def pop(self):
        if self.top == -1:
            return "Stack is empty"
        else:
            return self.stack[self.top]









