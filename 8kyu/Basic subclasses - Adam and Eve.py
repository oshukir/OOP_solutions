def God():
    return [Man("Adam"), Woman("Eva")]

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass
        
class Woman(Human):
    pass