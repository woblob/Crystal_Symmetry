from collections import deque
from itertools import combinations, product
import pickle
from time import time


class Queue:
    def __init__(self, names):
        self.queue = deque([el for el in product(names, repeat=2)])
        self.size = len(self.queue)

    def is_not_empty(self):
        return self.size != 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.queue.popleft()

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_not_empty():
            return self.dequeue()
        else:
            raise StopIteration


class mycontainer:
    def __init__(self, table, *names):
        self.tablica = table
        self.queue = Queue(names)
        self.uniques = set(names)
        self.origin = names
        self.calc()

    def calc(self):
        for name1, name2 in self.queue:
            wynik = self.tablica[name1][name2]
            if wynik not in self.uniques:
                self.expand(wynik)

    def expand(self, item):
        self.add_combinations(item)
        self.uniques.add(item)

    def add_combinations(self, addition):
        for name in self.uniques:
            self.queue.enqueue((name, addition))
            self.queue.enqueue((addition, name))
        self.queue.enqueue((addition, addition))

    def __repr__(self):
        return str(self.queue)

    def __contains__(self, item):
        return item in self.uniques


class Grupa:
    def __init__(self, konstruktory, all_syms):
        self.konstruktory = konstruktory
        self.all_syms = set(all_syms)

    def __repr__(self):
        return ' '.join((str(self.konstruktory), str(self.all_syms)))

    def __eq__(self, other):
        return self.all_syms == other.all_syms

    def __hash__(self):
        return hash(tuple(sorted(self.all_syms)))

    @classmethod
    def from_queue(cls, queue):
        return cls(queue.origin, queue.uniques)


class Timer:
    def __init__(self):
        self.start = time()
        self.mid = time()
        self.prev = 0

    def __call__(self, num):
        if num == self.prev:
            starter = round((time() - self.start) / 60, 1)
            mider = round(time() - self.mid, 1)
            self.mid = time()
            print(self.prev, starter, mider)
            self.prev += 1


if __name__ == "__main__":

    obliczanie_grup = '''    with open("data.pickle", "rb") as f:
        data = pickle.load(f)


    zespol = [set() for _ in range(500)]

    mytimer = Timer()
    for num1, num2 in combinations(range(len(data.columns)), 2):
        mytimer(num1)

        name1, name2 = data.columns[num1], data.columns[num2]
        tabliczka = mycontainer(data, name1, name2)

        num = len(tabliczka.uniques)
        zespol[num].add(Grupa.from_queue(tabliczka))


    for i, z in enumerate(zespol):
        if z != set():
            with open(f"wyniki zespolow/zespol {i}", "wb") as f:
                pickle.dump(z, f)'''

    with open("data.pickle", "rb") as f:
        data = pickle.load(f)

    l = [(i, name) for i, name in enumerate(data.columns)]

    with open("wyniki zespolow/zespoly_wszystkie.pickle", "rb") as f:
        zespoly = pickle.load(f)



    name1, name2 = data.columns[505], data.columns[524]
    tabliczka = mycontainer(data, name1, name2)


    print(tabliczka)
    ('3_mxmxx', 'm_xy0')