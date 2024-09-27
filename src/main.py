# src/my_class.py

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

# Instantiate the class and call the greet method
if __name__ == "__main__":
    person = MyClass("John")  # Create an instance of MyClass
    print(person.greet())      # Call greet and print the result