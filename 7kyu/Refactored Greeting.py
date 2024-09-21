class Person(object):
    def __init__(self, name):
        self.name = name
        
    def greet(self, name):
        return f"Hello {name}, my name is {self.name}"