class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


class Queue:

    def __init__(self):

        self.head = None

    def enqueue(self, value):

        new_node = Node(value)

        if self.head is None:

            self.head = new_node
            return

        node = self.head

        while node.next is not None:

            node = node.next

        node.next = new_node
        print("Appended new Node with value: ", node.next.value)

    def dequeue(self):

        if self.head is None:
            return None

        pop_node = self.head.value
        self.head = self.head.next
        return pop_node


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Pass" if (queue.dequeue() == 1) else "Fail")
print("Pass" if (queue.dequeue() == 2) else "Fail")
