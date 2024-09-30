# src/my_class.py

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

# This is just for testing purpose (i never tried using python class)
if __name__ == "__main__":
    person = MyClass("John") 
    print(person.greet())      
