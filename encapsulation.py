class base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"  # Private attribute

class Derived(base):
    def __init__(self):
    
        base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)  # trying to access private member of base class
obj1 = base()
print(obj1.a)  # trying to access private member of base class