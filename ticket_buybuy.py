import time
import random

class Ticket:
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

def simulate_line(till_movie, max_buytime):
    pq = Ticket()
    tic_sold = []

    for i in range(99):
        pq.enqueue("person" + str(i))

    t_end = time.time() + till_movie
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        random_wait_time = random.randint(0, max_buytime)
        time.sleep(random_wait_time)
        person = pq.dequeue()
        print(person," bought!")
        tic_sold.append(person)
    return tic_sold

sold = simulate_line(100, 1)
print(sold)