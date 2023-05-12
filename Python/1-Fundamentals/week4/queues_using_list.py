class Queue:

    def __init__ (self):

        self.items = []
    
    def enqueue (self, value):
        
        self.items.append(value)

    def dequeue (self):

        if len(self.items) == 0:
            return None
        
        return self.items.pop(0)
    
    def size (self):

        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Pass" if (queue.size() == 5) else "Fail")

queue.enqueue(5)
print("Pass" if (queue.size() == 5) else "Fail")

print("Pass" if (queue.dequeue() == 3) else "Fail")
print("Pass" if (queue.dequeue() == 2) else "Fail")
