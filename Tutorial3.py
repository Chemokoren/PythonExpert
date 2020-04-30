# Metclasses & How Classes Really Work
# Metaclasses define the rules for a class
# class Test:
#     pass
# print(Test)
# print(Test())
# print(type(Test()))
#print(type(Test)) # type class

# case 1: another way to define a class
#MyClass =type('MyClass',(),{})
#print(type(MyClass))

# case two

# MyClass =type('MyClass',(),{"x": 5})
# t =MyClass()
# t.wy="Hello"
# print(t.wy)

# case three
# class Foo:
#     def show(self):
#         print("hi")
#
# def add_attribute(self):
#     self.z =9
#
# MyClass =type('MyClass',(Foo,),{"x": 5, "add_attribute":add_attribute})
# t =MyClass()
# t.wy="Hello"
# t.add_attribute()
# print(t.show())
# print(t.z)


# Metaclasses
class Meta(type):
    def __new__(cls, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name,val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a [name.upper()] = val
        # return type(class_name, bases, attrs)
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x =5
    y =8

    def hello(self):
        print("hi")


d =Dog()
print(d.X)
print(d.HELLO())
