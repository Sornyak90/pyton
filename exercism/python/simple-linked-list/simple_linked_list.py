class EmptyListException(Exception):
    def __init__(self, message="The list is empty."):
        super().__init__(message)


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def value(self):
        return self.value

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, values=[]):
        self.head = None
        for val in reversed(values):
            self.push(val)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def head(self):
        if self.head is None:
            raise EmptyListException()
        return self.head.value()

    def push(self, value):
        new_node = Node(value=value, next_node=self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise EmptyListException()
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def reversed(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self
sut = LinkedList()
print(sut.head())
