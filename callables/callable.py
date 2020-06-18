# A callable is something that can be called. 
# The callable() method takes only one argument

# callable() method checks if the argument is either of the two:
# - An instance of a class with a __call__ method.
# - Is of a type that has a which indicates callability
#    such as in functions, methods etc.

print("Check if __call__ exist in a class - hasattr(class,'__call__')", hasattr(int,'__call__'))
def Geek(): 
    return 5

class Geek2(): 
    def __call__(self): 
        print("""The __call__ shoudld exist when callable() used, else will throw error.
        __call__ will always be invoked with object""") 
    
    def test(self):
        print("test")

# an object is created of Geek()
obj = Geek 
print('callable(Geek): ', callable(Geek))
print('callable(obj): ', callable(obj))

GeekObject = Geek2() 
print('callable(Geek2): ', callable(Geek2))
GeekObject()

print('callable(5 * 5): ', callable(5 * 5))