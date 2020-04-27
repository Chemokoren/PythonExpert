# Dunder/Magic Methods & The Python Data Model

x = [1, 2, 3]
y = [4, 5]

print(x + y)
print(type(x))
# print(x * y)

#
# second
#
import inspect


# print(inspect.getsource(list))


#
# third
#

class Person:
    def __init__(self, name):
        self.name = name

    # allows us to define string representation of an object

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        self.name = self.name * x

    def __call__(self, y):
        print("called this function", y)

    def __len__(self):
        return len(self.name)


p = Person("tim")
# print(p)

# p * 4
# print(p)
# p(4)

print(len(p))

#
# example 3
#
from queue import Queue
import inspect

q = Queue()
print(q)

print(inspect.getsource(Queue))

#
# example 4 -update of 3
#
from queue import Queue as q
import inspect


class Queue(q):
    def __repr__(self):
        return f"Queue({self.qsize()})"
    def __add__(self, item):
        self.put(item)
    def __sub__(self, item):
        self.get()

qu = Queue()
print(qu)

#
# example 5
#
qu  =Queue()
qu + 9
print(qu)

#
#example 6
#
qu  =Queue()
qu + 9
qu + 9
qu + 9
qu -None
print(qu)
