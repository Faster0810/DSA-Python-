import ctypes

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Empty Queue"
        else:
            self.front = self.front.next
            return None
    def is_empty(self):
        if self.front is None:
            return self.front is None

    def size(self):
        temp = self.front
        count=0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def front_item(self):
        if self.front is None:
            return "Empty Queue"
        else:
            return self.front.data

    def traverse(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def rear_item(self):
        if self.rear is None:
            return "Empty Queue"
        else:
            return self.rear.data




