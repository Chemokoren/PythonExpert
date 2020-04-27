def make_class(x):
	class Dog:
		def __init__(self,name):
			self.name =name

		def print_val(self):
			print(x)

	return Dog

cls =make_class(10)
# print(cls)
d =cls("Tim")
print(d.name)
d.print_val()

#
# example 2
#

for i in range(10):
	def show():
		print(i *2)

	# show()

show()

#
# example 3
#

def func(x):
	if x == 1:
		def rv():
			print("X is equal to 1")
	else:
		def rv():
			print("X is not 1")
	return rv

new_func = func(2)
new_func()
print(id(new_func)) #memory address

#
# example 3
#
import inspect

print(inspect.getmembers(new_func))
print(inspect.getsource(new_func))

#
# example 4
#
from queue import Queue

print(inspect.getsource(Queue))
