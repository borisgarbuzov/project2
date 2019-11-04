
class MyClass:
    
    def __init__ (self, a):
        print("init method")
        
    def __new__ (self, a):
        print("new method, a =", a)
        self.field_1 = a

    def __del__ (self):
        print("del method")
        
    def my_method (self):
        print("my_method, field_1 =", self.field_1)

class Class2(object):
    
    def __del__ (self):
        print("del method of Class2")    
        # object.__del__(self)
        
my_class = MyClass(a = 5)
# AttributeError: 'NoneType' object has no attribute 'my_method'
# my_class.my_method()

my_class2 = Class2()
my_class2.__del__()
my_class2.__del__()

print(dir(int))
print ()
print(dir(MyClass))
my_class_3 = MyClass(a = 3)
print ()
# print(my_class_3.__dict__)
num=10
print(num + 5)
print(num.__add__(5))

if __name__ == "__main__":
    print("name is main")


















        