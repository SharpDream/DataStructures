from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


class FOS:

    def __init__(self):
        self.tasks = Queue()

    def order(self, orders: list):
        for elements in orders:
            self.tasks.enqueue(elements)

    def serve(self, food):
        q = self.tasks
        i = q.buffer.index(food)
        if i == 0:
            while x + 1 < q.size():
                q.buffer[x] = q.buffer[x + 1]
                x += 1
            q.dequeue()
            return
        elif i == q.size():
            q.dequeue()
        else:
            for x in range(i, q.size()):
                if x + 1 < q.size(): q.buffer[x] = q.buffer[x + 1]
        q.dequeue()
