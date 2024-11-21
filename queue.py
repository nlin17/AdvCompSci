class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    def display(self):
        print(self.items)

teddy = Queue()
teddy.enqueue(1)
teddy.enqueue(2)
teddy.enqueue(3)
teddy.enqueue(4)
teddy.display()
ben = teddy.dequeue()
teddy.display()
print(ben)
