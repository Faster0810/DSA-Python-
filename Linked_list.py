class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length


    def insert(self, value):
#create new node
        new_node = Node(value)
#create connection
        new_node.next = self.head
#reassign head
        self.head = new_node
        self.length = self.length + 1


    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "->"
            current = current.next
        return result[:-2]

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next is not None:
            current = current.next

    #you are at the last node
        current.next = new_node

    def insert_after(self,after,value):
        new_node = Node(value)
        current = self.head

        while current.next is not None:
            if current.data == after:
                new_node.next = current.next
                current.next = new_node
                self.length = self.length + 1
                return
            current = current.next
        print("Item not found")

    def clear(self):
        self.head = None
        self.length = 0

    def delete_head(self):
        if self.head is None:
            return "Empty list"

        self.head = self.head.next
        return None

    def pop(self):
        if self.head is None:
            return "Empty list"
        current = self.head
        if current.next is None:
            return self.delete_head()
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.length = self.length - 1
        return None

    def remove(self, value):
        if self.head is None:
            return "Empty list"
        if self.head.data == value:
            return self.delete_head()
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                break
            current = current.next
        if current.next is None:
            return "Item not found"
        else:
            current.next = current.next.next

    def search(self, item):
        current = self.head
        position = 0
        while current is not None:
            if current.data == item:
                return position
            current = current.next
            position = position + 1

        return "Item not found"

    def __getitem__(self, index):
        current = self.head
        position = 0
        while current is not None:
            if position == index:
                return current.data
            current = current.next
            position = position + 1
        return "Index Error!!"

    def replace_max(self, value):
        current = self.head
        max = current

        while current is not None:
            if current.data > max.data:
                max = current
            current = current.next

        max.data = value

    def sum_odd_nodes(self):
        current = self.head
        counter = 0
        result = 0
        while current is not None:
            if counter % 2 != 0:
                result+=current.data
            counter+=1
            current = current.next

        print("Sum of odd nodes: ",result)


    def reverse(self):
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


