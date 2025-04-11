class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, n_value):
        self.items.insert(0, n_value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
if queue.is_empty():
    print("queue is empty...")

for c in "ポセイドン":
    queue.enqueue(c)

print("size = ",queue.size())

for i in range(3):
    print(queue.dequeue())

print("size = ",queue.size())


