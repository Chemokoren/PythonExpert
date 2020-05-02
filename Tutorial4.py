# This tutorial is about decorators
def func1(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")

    return wrapper()
    # return wrapper

x =func1("hello")
# x =func("hello")
# print(x)
# x()


##############################################################################
# Approach 2
##############################################################################


def funcApproach2(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")

    return wrapper

def func2():
    print("I am func 2")
def func3():
    print("I am func 3")

print("Beginning of approach2")
x =funcApproach2(func2)
y =funcApproach2(func3)
print(x)
x()
y()

##############################################################################
# Approach 3
##############################################################################

print("Beginning of Approach 3")
func3 =funcApproach2(func3)
func2 =funcApproach2(func2)
func3()
func2()


##############################################################################
# Approach 4
##############################################################################
print("Beginning Approach  4")

@funcApproach2
def func4():
    print("I am function 4")

@funcApproach2
def func5():
    print("I am function 5")

func4() # should have same parameters as the wrapper function
func5()


##############################################################################
# Approach 5
##############################################################################
print("Beginning of approach 5")
def funcApproach5(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args,**kwargs)
        print("Ended")
        return rv
    return wrapper

@funcApproach5
def func51(x,y,z):
    print(x)
    return z

@funcApproach5
def func52():
    print("I am func 52")

# func51(5)
func52()
x = func51(5,6,23)
print(x)


##############################################################################
# Approach 6
##############################################################################
print("Beginning of approach 6")

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start =time.time()
        rv =func()
        total =time.time() -start
        print("Time: ", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(1):
        pass
        # print(_)
@timer
def test2():
    time.sleep(2)

test()
test2()
