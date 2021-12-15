from threading import Thread
from time import sleep
from random import randint


class Counter(Thread):
    """Class based daemon"""
    def __init__(self, num):
        super().__init__(daemon=True)
        self.count = num
        self.name = f'{self.count} counter object'

    def run(self):
        while self.count > 0:
            print(self.name, self.count)
            self.count -= 1
            sleep(randint(2, 5))


def count_up():
    """function based daemon (see Thread assignment below)"""
    c = 0
    while c < 10:
        c += 1
        print(f'count up - {c}')



# main logic
c1 = Counter(5)
c2 = Counter(10)
c3 = Counter(20)

c1.start()
c2.start()
c3.start()

t = Thread(target=count_up, daemon=True)
t.start()

data = input(f'Enter your name: ')
print(f'Hi {data}')
data = input(f'Enter a color: ')
print(f'I like {data}')
data = input(f'Enter a food: ')
print(f'{data}, yum!')
